import os
import random
import google.generativeai as genai
from datetime import datetime

# 1. 제미나이 설정
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY missing in Secrets.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 저장 경로 설정
posts_dir = "content/posts"
os.makedirs(posts_dir, exist_ok=True)

# 3. 주제 카테고리 (더 구체적이고 흥미로운 주제들)
topics = [
    "Secret Kitchen Hacks used by Professional Chefs",
    "Psychological Productivity Tricks to beat Procrastination",
    "Hidden iPhone & Android Features that save hours",
    "Smart Minimalist Budgeting for Urban Living",
    "Science-backed Morning Routines for Peak Energy",
    "Travel Hacks for Finding Cheap Flights and Hotels",
    "Eco-friendly Life Hacks that actually save Money"
]
selected_topic = random.choice(topics)

# 4. 고품질 전문가 페르소나 프롬프트 (핵심!)
prompt = f"""
System Role: You are a world-class English lifestyle blogger and SEO expert with 10+ years of experience.
Task: Write a high-quality, engaging, and professional blog post about '{selected_topic}'.

[Quality Standards]
1. Human-like Writing: Use natural transitions (e.g., "To be honest," "Here's the kicker," "Interestingly"). Avoid AI-clichés.
2. Value-Driven: Provide specific, actionable advice. Don't be vague.
3. SEO Excellence: Identify the most searched keyword for this topic and use it in the title, first 100 words, and subheadings.
4. Readability: Use short sentences, bullet points, and **bold text** for key insights.

[Structure]
- Title: A high-click-through-rate (CTR) title with a number or a power word.
- Introduction: Hook the reader by addressing a common pain point.
- Body: 3-4 detailed sections with H2 and H3 subheadings.
- Pro-Tip Section: A unique, "insider" tip that adds extra value.
- Conclusion: A brief wrap-up with a call to action.

[Output Format: Hugo Markdown]
---
title: "[Expert SEO Title]"
date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')}
draft: false
tags: ["List 5-7 trending, specific SEO tags"]
description: "[Write a compelling 150-character meta description for Google Search]"
---

[Post Content Starts Here]
"""

# 5. 글 생성 및 저장
try:
    response = model.generate_content(prompt)
    # 파일명을 제목 기반으로 하면 좋지만, 일단 안전하게 타임스탬프로 생성
    filename = f"{posts_dir}/post-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"✅ High-Quality Post Generated: {filename}")
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
