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

# 3. 주제 카테고리
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

# 4. 고품질 전문가 페르소나 프롬프트 (수정 없음)
prompt = f"""
System Role: You are a world-class English lifestyle blogger and SEO expert with 10+ years of experience.
Task: Write a high-quality, engaging, and professional blog post about '{selected_topic}'.

[Quality Standards]
1. Human-like Writing: Use natural transitions. Avoid AI-clichés.
2. Value-Driven: Provide specific, actionable advice.
3. SEO Excellence: Use keywords in title and subheadings.
4. Readability: Use short sentences and bold text.

[Structure]
- Title: A high-click-through-rate (CTR) title.
- Introduction: Hook the reader.
- Body: 3-4 sections with H2/H3.
- Pro-Tip Section: Insider tip.
- Conclusion: Brief wrap-up.

[Output Format: Hugo Markdown]
---
title: "[Expert SEO Title]"
date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')}
draft: false
tags: ["List 5-7 trending, specific SEO tags"]
description: "[Write a compelling 150-character meta description]"
---

[Post Content Starts Here]
"""

# 5. 글 생성 및 저장 (파일 생성까지만 수행)
try:
    response = model.generate_content(prompt)
    if not response.text:
        raise ValueError("Gemini response is empty.")
        
    filename = f"{posts_dir}/post-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"✅ Success: {filename} created.")

except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
