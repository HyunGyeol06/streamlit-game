import streamlit as st
import json
import game

def show_game_info(name):
    json_string = game.get_game_info(name)

    game_info = json.loads(json_string)

    st.write("게임 이름:  ",game_info["game_name"])
    st.write("게임 설명:  ", game_info["game_desc"])
    st.video(game_info["game_video"])






st.set_page_config(page_title="게임 정보")

st.title("게임 정보 찾기")

game_name = st.text_input("게임 이름")

clicked = st.button("채찍피티의 게임 정보 찾기")

if clicked:
    show_game_info(game_name)
    st.write("\n\n게임 정보 찾기가 끝났어요.")