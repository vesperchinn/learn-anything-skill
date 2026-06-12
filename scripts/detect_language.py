#!/usr/bin/env python3
"""Detect the default locale from user input.

Infers whether the user is likely an English or Chinese speaker based on the
characters and words in their input. Used at intake to set {locale},
{interface_language}, and {learning_language} defaults before the user
explicitly confirms or overrides.

Usage:
    python3 detect_language.py "I want to learn AI agents"
    # → {"locale": "en-US", "interface_language": "English", "learning_language": "English"}

    python3 detect_language.py "我想学习营养学"
    # → {"locale": "zh-CN", "interface_language": "中文", "learning_language": "中文"}

    python3 detect_language.py "用中文对话，但学习仓库用英文"
    # → {"locale": "zh-CN", "interface_language": "中文", "learning_language": "English"}

Exit codes: 0 = en-US, 1 = zh-CN, 2 = mixed/ambiguous.
"""

import json
import re
import sys


# Unicode ranges for CJK characters (simplified detection)
CJK_RANGES = [
    (0x4E00, 0x9FFF),    # CJK Unified Ideographs
    (0x3400, 0x4DBF),    # CJK Unified Ideographs Extension A
    (0x20000, 0x2A6DF),  # CJK Unified Ideographs Extension B
    (0xF900, 0xFAFF),    # CJK Compatibility Ideographs
]

# Common English words that signal English intent even in mixed input
ENGLISH_SIGNAL_WORDS = [
    "english", "learn", "learning", "study", "want", "help",
    "start", "create", "build", "make", "teach", "explain",
]

# Common Chinese words that signal Chinese intent even in mixed input
CHINESE_SIGNAL_WORDS = [
    "学习", "想学", "帮我", "教我", "怎么", "如何", "什么",
    "开始", "创建", "搭建", "生成", "了解", "入门",
]

# Phrases that indicate a mixed-language preference
MIXED_SIGNALS = [
    r"用中文.*英文",
    r"用英文.*中文",
    r"chinese.*english",
    r"english.*chinese",
    r"interface.*chinese",
    r"interface.*english",
    r"对话.*中文.*仓库.*英文",
    r"对话.*英文.*仓库.*中文",
]


def count_cjk(text: str) -> int:
    """Count the number of CJK characters in text."""
    count = 0
    for ch in text:
        cp = ord(ch)
        for lo, hi in CJK_RANGES:
            if lo <= cp <= hi:
                count += 1
                break
    return count


def count_latin(text: str) -> int:
    """Count the number of Latin alphabet characters in text."""
    return sum(1 for ch in text if ch.isalpha() and ord(ch) < 128)


def detect_mixed(text: str) -> bool:
    """Check if the text contains mixed-language signals."""
    text_lower = text.lower()
    return any(re.search(pattern, text_lower) for pattern in MIXED_SIGNALS)


def parse_mixed_preference(text: str) -> dict:
    """Parse a mixed-language input to extract interface and learning languages."""
    text_lower = text.lower()

    # Default for mixed: interface = Chinese (detected from CJK in "用中文对话"),
    # learning = English (detected from "学习仓库用英文")
    interface_lang = "中文"
    learning_lang = "English"

    if re.search(r"用英文.*中文|english.*chinese|interface.*english", text_lower):
        interface_lang = "English"
        learning_lang = "中文"

    # Determine locale from interface language
    locale = "en-US" if interface_lang == "English" else "zh-CN"

    return {
        "locale": locale,
        "interface_language": interface_lang,
        "learning_language": learning_lang,
    }


def detect(text: str) -> dict:
    """Detect locale from user input text.

    Returns a dict with locale, interface_language, and learning_language.
    """
    if not text or not text.strip():
        # Empty input → default to English
        return {
            "locale": "en-US",
            "interface_language": "English",
            "learning_language": "English",
        }

    text = text.strip()

    # Check for explicit mixed-language signals first
    if detect_mixed(text):
        return parse_mixed_preference(text)

    cjk_count = count_cjk(text)
    latin_count = count_latin(text)

    # Strong CJK presence → Chinese
    if cjk_count > 0 and cjk_count >= latin_count * 0.5:
        return {
            "locale": "zh-CN",
            "interface_language": "中文",
            "learning_language": "中文",
        }

    # Mostly Latin → English
    if latin_count > 0 and latin_count > cjk_count * 2:
        return {
            "locale": "en-US",
            "interface_language": "English",
            "learning_language": "English",
        }

    # Ambiguous or balanced → English default
    return {
        "locale": "en-US",
        "interface_language": "English",
        "learning_language": "English",
    }


def main():
    if len(sys.argv) < 2:
        # Read from stdin if no arguments
        text = sys.stdin.read()
    else:
        text = " ".join(sys.argv[1:])

    result = detect(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))

    # Exit code for scripting
    if result["locale"] == "zh-CN":
        if result["learning_language"] == "English":
            sys.exit(2)  # mixed
        sys.exit(1)  # zh-CN
    sys.exit(0)  # en-US


if __name__ == "__main__":
    main()
