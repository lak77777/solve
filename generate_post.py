import os
import random
import google.generativeai as genai
from datetime import datetime

# 1. 설정
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 현재 포스팅 개수 확인 (글쓰기 실력 성장을 위해)
posts_dir = "content/posts"
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)
post_count = len(os.listdir(posts_dir))

# 3. 숙련도 결정 (글 개수에 따라 레벨업)
if post_count < 50:
    level = "Beginner (Simple, clear, friendly)"
elif post_count < 200:
    level = "Intermediate (Professional, detailed, use idioms)"
else:
    level = "Expert (Authoritative, sophisticated vocabulary, deep insights)"

# 4. 중복 방지를 위한 다양한 주제 리스트
# (제미나이에게 이 리스트 중 하나를 주되, 내부에서 더 구체적인 소주제를 잡으라고 명령)
broad_topics = [
    "Unexpected Home Maintenance Hacks",
    "Psychological Productivity Tricks",
    "Hidden Smartphone Features for Efficiency",
    "Science-backed Health & Sleep Hacks",
    "Zero-waste & Eco-friendly Living Tips",
    "Smart Social Skills & Communication Life-hacks",
    "Minimalist Finance & Micro-saving Techniques",
    "Advanced Travel Hacks for Frequent Flyers"
]
selected_broad_topic = random.choice(broad_topics)

# 5. 성장형 + 중복방지 + 고품질 프롬프트
prompt = f"""
Current Blog Level: {level} (Post #{post_count + 1})
Main Topic Category: {selected_broad_topic}

You are a native English blogger. Your writing skills improve as you write more posts. 
Today, you are at the '{level}' stage. 

[Mission]
1. Pick a VERY SPECIFIC and UNIQUE sub-topic within '{selected_broad_topic}' that people are curious about. 
2. Ensure this specific idea is not a cliché. Avoid common tips everyone knows.
3. Write a high-quality post in English.
4. As a level '{level}' writer, use appropriate vocabulary and sentence structures.

[SEO & Structure]
- Use a catchy, SEO-optimized title.
- Meta description (1-2 sentences).
- Engaging intro, detailed body with H2/H3 tags, and a practical 'Pro-Tip' section.
- Use 5-8 trending SEO tags.

[Output Format: Hugo Markdown]
---
title: "[Title]"
date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')}
draft: false
tags: [tags]
description: "[description]"
---

[Content]
"""

# 6. 생성 및 저장
response = model.generate_content(prompt)
filename = f"{posts_dir}/lifehack-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"✅ {level} level post generated: {filename}")
