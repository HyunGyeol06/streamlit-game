from openai import OpenAI
import streamlit as st


def find_game(
        genre,
        age,
        is_free,
        call_stack
):
    if call_stack > 5:
        return "게임을 찾을 수 없습니다. 다시 시도해주세요."

    global messages
    client = OpenAI(
        api_key=st.secrets["openai_key"]
    )

    messages = [
        {"role": "system", "content": "You know every game in the world. Please find one to three games for me."},
        {"role": "system",
         "content": "Don't Let me know fake games. Let me know only real games. And explain the games to me."},
        {"role": "user",
         "content": f"게임을 추천해주세요. 장르는 {genre}, 연령층은 {age}, 무료인 게임만 추천해주세요." if is_free else f"게임을 추천해주세요. 장르는 {genre}, 시대는 {age}입니다."}
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=5000,
        temperature=1,
    )
    summary = response.choices[0].message.content

    is_real_message = [
        {"role": "system",
         "content": "You are the master of the games. Please tell me if this game is real or not. Answer only 'real' or 'fake'."},
        {"role": "user", "content": f"Is f{summary} real?"}
    ]

    real_response = client.chat.completions.create(
        model="gpt-4",
        messages=is_real_message,
        max_tokens=500,
        temperature=0.2,
    )
    if real_response.choices[0].message.content == "fake":
        return find_game(genre, age, is_free, call_stack=call_stack + 1)
    else:
        return summary
