import game
import streamlit as st


def create_game(
        genre1,
        age1,
        is_free1
):
    st.write("새게챼고의 게이머 채찍피티가 게임을 찾고있어요." )

    game_name = game.find_game(
        genre1,
        age1,
        is_free1,
        1
    )

    if game_name != "":
        st.write("매우 엄청나고 으메이징한 게임:\n", game_name)


# -------- main page ---------

st.set_page_config(page_title="게임 찾기", page_icon="🎮")

st.title("게임찾기")

genre = st.selectbox("장르", ["액션", "어드벤처", "RPG", "JPRG", "스포츠", "레이싱", "시뮬레이션", "전략", "퍼즐", "음악", "캐주얼", "아케이드"])
age = st.selectbox("연령대", ["전체", "7세 이상","12세 이상", "15세 이상", "18세 이상"])
is_free = st.checkbox("무료인 게임만")

clicked = st.button("채찍피티의 게임찾기")

if clicked:
    create_game(genre, age, is_free)
    st.write("\n\n게임 찾기가 끝났어요.")
