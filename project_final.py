import os
import shutil as copycat
import sys
import time
import pyttsx3 
from pyfiglet import Figlet
import random
import pyjokes

engine = pyttsx3.init() 
rate = engine.getProperty('rate')   
engine.setProperty('rate', 155)
def ls():
    items = os.listdir()
    print(items)

def pwd(): 
    print(f"Current working directory:{os.getcwd()}")

def cd(path):
    try:
        os.chdir(path)
        print(f"\nDirectory changed to: {os.getcwd()} \n")
    except FileNotFoundError:
        print(f"\n path tersebut tidak ada : {path} \n")

def mkdir(path):
    try:
        os.mkdir(path)
        print(f"\n buat direktori baru : {path} \n")
    except FileExistsError:
        print(f"\n {path} \n")

def rmdir(dirName):
    try:
        os.rmdir(dirName)
        print(f"\nDirectory terhapus: {dirName} \n")
    except FileNotFoundError:
        print(f"\nDirectory tidak ditemukan {dirName} \n")
    except OSError:
        print(f"\nDirectory {dirName} tidak kosong \n")

def touch(fileName):
    try:
        with open(fileName, 'a'):
            pass
        print(f"\n file : {fileName} berhasil dibuat\n")
    except FileExistsError:
        print(f"\n {fileName} \n")

def frieren():
    frieren = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠀⡔⠀⠀⠀⠀⠀⠰⡰⡀⠀⠀⢳⣄⠀⠀⠐⠆⠀⠀⠀⠀⠀⠐⢆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⡔⠛⠛⢯⡉⠑⠒⡤⠊⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⣀⣀⡀⠤⠤⠤⠤⠤⠼⠤⢴⣃⡀⠀⠀⠀⠀⠀⢳⢱⡀⠀⠀⢳⡱⣄⠀⠀⠐⢄⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⠋⠀⠀⣀⣀⢳⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠦⣄⠀⠈⡇⢣⠀⠀⠀⢣⠈⢦⠀⠀⠀⠑⢄⠀⠀⠀⠀⢣⡀⠀⠀
    ⠀⠀⠀⢠⣃⠴⠊⠉⢀⡴⡻⢹⠘⠢⢄⣀⣀⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣱⠈⡇⠀⠀⠈⣇⠀⢷⡀⠀⠀⠈⠳⡀⠀⠀⠀⢳⡀⠀
    ⠀⠀⢀⠏⠁⠀⠀⢠⠎⡰⠁⠘⡄⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣽⠀⠀⠀⢸⠀⢸⡵⡀⠀⠀⠀⠘⢆⠀⠀⠀⢣⠀
    ⠀⠀⡜⠀⠀⠀⢠⠏⢰⡇⠀⠀⢑⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠒⠒⠒⠒⠂⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠈⡆⢸⢇⢱⡀⠀⠀⠀⠈⢦⠀⠀⠈⠀
    ⠀⢠⠃⠀⠀⠀⡞⠀⣿⠁⠀⢠⠎⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠄⠀⠀⠤⠤⣀⡈⠑⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⡇⢸⢸⠀⢧⠀⠀⠀⠀⠈⢧⣀⠴⠊
    ⠀⠈⠀⠀⠀⢸⠁⢸⢸⠀⣰⠃⠀⠀⠀⠀⠀⠀⡴⠋⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⢄⠑⢄⠀⠀⠀⢦⠀⠀⠀⠀⠀⠀⠈⢦⡇⢸⠘⡄⠘⡆⠀⠀⣀⠴⠊⠁⢀⡰
    ⠀⠀⠀⠀⠀⡇⠀⡎⢸⢠⠃⠀⠀⠀⠀⠀⢀⡞⠀⢠⠖⠁⠀⢤⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣵⣄⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⢳⡌⠀⡇⠀⢷⡠⠊⠁⠀⣠⡔⡏⡜
    ⠀⠀⠀⠀⢸⠀⠀⡇⢸⡎⠀⠀⠀⠀⠀⢀⡎⠀⡴⠁⠀⠀⠀⠀⢹⢦⡈⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⣄⠀⠹⡄⠀⠀⠀⠀⠀⠀⢻⣠⣃⡴⠋⠀⣠⠔⠊⠀⡇⢩⠞
    ⠀⠀⠀⠀⡏⠀⠀⡇⡸⠀⠀⠀⠀⠀⠀⡞⠀⡜⠁⠀⠀⠀⠀⠀⢸⡆⠛⠦⡈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠘⡄⠀⠀⠀⠀⠀⠀⢻⡊⠀⣠⠊⠁⠀⠀⡜⢰⡇⠀
    ⠀⠀⠀⢠⠃⠀⠀⣇⠇⠀⠀⠀⠀⠀⢰⠁⡸⠁⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠈⠓⠬⡑⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠹⡀⠀⠀⠀⠀⢠⡀⢣⡜⠁⠀⠀⠀⢰⢱⠃⢸⠀
    ⠀⠀⠀⢸⠀⠀⠀⢹⢠⠀⠀⠀⠀⠀⢸⢠⠃⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠈⠑⠲⠭⣲⡴⢖⣒⡆⠀⠀⠀⠀⠀⢧⠀⢳⠀⠀⠀⠀⠀⢧⠈⡆⠀⠀⠀⢠⢇⠇⠀⠸⠀
    ⠀⠀⠀⡎⠀⠀⠀⡎⢸⠀⠀⠀⠀⠀⢿⡜⠀⠀⠀⠀⠀⠀⡀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⢉⡡⠞⠛⢭⣭⣥⠤⠤⠚⡆⠈⣦⠆⠀⠀⠀⠸⠀⢳⠀⠀⠀⡞⡞⠀⠀⠀⠀
    ⠀⠀⠀⡇⠀⠀⢰⡇⢸⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⢠⡏⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠉⣠⠖⠋⠁⢀⣤⣤⣦⣔⣳⡾⢳⠀⠀⠀⠀⠀⡇⢸⣀⡠⠊⣼⢸⠀⠀⠀⠀
    ⠀⠀⠀⡇⠀⠀⢸⡇⢸⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⢀⡮⣵⠓⢠⡤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡝⢀⣴⣯⣿⡿⣛⣿⣿⣻⡄⢸⠀⠀⠀⠀⢀⡇⠸⠣⣄⡜⠁⢸⠀⠀⠀⠀
    ⠀⠀⠀⡇⠀⠀⡇⠇⢸⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⢴⣱⣷⣁⢤⣊⣀⡀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⡿⠁⢿⣄⡿⠟⣸⡛⡇⡎⠀⠀⠀⠀⢸⣵⢐⣴⠋⠀⠀⠈⠀⠀⠀⠀
    ⠯⣉⠀⠓⠒⠒⠃⢼⠸⡄⠀⠀⠀⠀⠀⠸⡀⠀⢀⣼⠏⡠⠞⠁⠀⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠐⣲⡾⠏⠀⣧⢣⠀⠀⠀⠀⡎⣿⣼⢸⡆⠀⠀⠀⠀⠀⠀⠀
    ⠣⢌⡻⣍⣱⠒⡠⢼⠀⡇⠀⠀⠀⠀⠀⠀⢧⡠⠚⠁⠘⢁⣤⣶⣶⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⢸⠀⠀⠀⢰⢹⡜⣿⣿⢣⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠉⢲⣄⡀⢣⡈⡇⢹⠀⠀⠀⠀⠀⢢⠘⡄⢄⣀⣠⣾⠟⢹⣏⡈⣿⡿⣿⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢸⠀⠀⢠⢃⡏⡇⡿⣹⢸⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢸⣡⠉⡶⣍⢳⠀⣇⠀⠀⠀⠀⠈⣆⠻⣄⠀⠉⠙⢦⣀⠉⠹⠧⣤⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⢸⠀⣠⠃⡞⡇⡇⠀⡟⡞⠁⠀⠀⠀⠀⢀⠀
    ⠀⠀⠀⠀⡿⠀⡇⠀⠹⡄⢸⡄⠀⠀⠀⠀⠘⡄⢣⠳⣄⠀⠀⠀⠋⠚⠙⠉⠁⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⢸⡰⠁⡜⠁⡗⢸⠀⢹⠃⠀⠃⠀⠀⠀⠸⠀
    ⠀⠀⠀⠀⢧⡇⠃⠀⠀⢳⠈⡿⡀⠀⠀⠀⠀⠘⣆⢳⡌⣢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⣼⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⢁⡞⠀⢰⠃⣼⠀⢸⠀⠀⠀⠀⠀⠀⡇⠀
    ⠀⠀⠀⠀⢸⢡⠀⠀⠀⠈⢧⢱⢱⡀⠀⠀⠀⠀⢹⢫⣫⡁⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⢀⡾⠁⠀⡜⢠⢻⠀⢸⠀⠠⠀⠀⠀⢠⠃⠀
    ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠈⣎⢿⠙⣄⠀⠀⠀⠈⣿⢯⠳⣄⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠐⠊⠁⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⣼⢥⠏⡸⠀⡎⡄⠀⠀⠀⠀⡸⠀⠀
    ⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⢸⢞⣞⡞⢳⡀⠸⡄⠛⡌⣦⠏⠷⠄⠀⠑⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⣠⡾⡿⠋⢀⡇⢀⢧⠃⠀⠀⠀⠀⡇⠀⠀
    ⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⢸⢸⣿⣦⣞⠏⠢⣱⢀⢧⢹⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠠⠤⠤⢀⣀⣀⣀⠀⠀⠀⢀⡠⠞⠁⢀⣠⣾⣿⢾⡀⠀⠘⠀⢸⡜⠀⠀⠀⠀⠘⠀⡸⠀
    ⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⢸⢸⠿⡫⠋⠀⠀⠈⡟⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⢿⣿⠯⠥⠤⠒⣎⡿⢿⡿⠳⡀⠑⣄⠀⠀⣏⠃⠀⠀⠀⠀⠀⢠⠃⠀
    ⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⢸⡈⠉⠀⠀⠀⠀⠀⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⠍⢹⠉⢹⠀⠀⢀⣳⡄⠙⢄⠈⢢⣰⡻⠀⠀⠀⠀⠀⠀⡞⠀⠀
    ⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⠀⣸⠎⠉⠓⠢⢜⣆⠈⢣⡀⢹⠇⠀⠀⠀⠀⠀⢠⠃⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡿⡄⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡃⢸⡴⢻⠀⣀⣠⣤⣶⣾⣧⡀⠑⡼⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀
    ⠀⠀⡆⠀⠀⠀⠀⢸⢣⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠟⡇⢸⣟⢿⡿⠿⠿⠿⠛⣷⣄⡇⠀⠀⠀⠀⠀⠀⡇⠀⡴⠀
    ⠀⠀⢱⠀⠀⠀⠀⠈⡎⡆⠀⠀⡷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡇⢸⡇⠀⠀⣀⡠⠤⠖⠛⠚⡇⠀⢠⠀⠀⠀⢠⠃⢰⠃⠀"""
    print(frieren)

def helepp():
    print("ls: Menampilkan daftar file dan folder di direktori saat ini.")
    print("pwd: Menampilkan direktori kerja saat ini.")
    print("cd: Mengubah direktori kerja.")
    print("mkdir: Membuat direktori baru.")
    print("rmdir: Menghapus direktori (jika kosong).")
    print("touch: Membuat file kosong baru.")
    print("rm: Menghapus file.")
    print("cp: Menyalin file dari satu lokasi ke lokasi lain.")
    print("mv: Memindahkan atau mengganti nama file/direktori.")
    print("help: Menampilkan list perintah yang ada dan fungsinya.")
    print("clear: Membersihkan layar terminal.")
    print("exit: Keluar dari CLI.")
    print("Extra :")
    print("art: Membuat ascii teks.")
    print("janken: Melakukan permainan Batu Gunting Kertas")
    print("jokes: untuk menampilkan lelucon")
    
def rm(file):
    try:
        os.remove(file)
        print(f"\n file : {file} berhasil dihapus\n")
    except FileNotFoundError:
        print(f"\n {file} \n")
    

def cp(src, dest):
    try:
        if os.path.isdir(src):
            copycat.copytree(src, dest, dirs_exist_ok=True)
            print(f"\n directory : {src} berhasil disalin ke {dest}\n")
        else:
            copycat.copy2(src, dest)
            print(f"\n file : {src} berhasil disalin ke {dest}\n")
    except FileNotFoundError:
        print(f"\n error {src} \n")
        

def mv(src, dest):
    try:
        copycat.move(src, dest)
        print(f"\n file : {src} berhasil dipindahkan ke {dest}\n")
    except FileNotFoundError:
        print(f"\n {src} \n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def art():
    textart = input("Masukkan text yang ingin dijadikan art : ")
    art = Figlet(font='banner3-D')
    print(art.renderText(textart))
    
ganyu = """  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠒⣀⡒⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⣉⡴⠶⠛⠋⠉⠙⠻⣦⠑⡄⠀⠀⠀⠀⠀⠀⢀⡠⠤⠐⠒⠒⠒⠀⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⣠⠞⠉⠀⠀⠀⣠⣤⣤⣄⠈⣧⠸⣀⣀⣀⡠⠔⢊⣡⣤⣶⣶⣾⣿⣷⣶⣦⣌⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⣰⠃⠀⠀⠀⣠⠞⣉⣤⣤⠌⢳⣸⣄⣤⣤⣤⣤⣶⢻⣿⡿⠿⠛⠋⠉⠉⠉⠛⠻⣷⣄⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⠇⠀⠀⠀⢰⠃⡼⠓⢉⣠⡶⠟⠋⠉⠀⠀⢠⣿⣡⡾⠋⢀⣴⡞⢁⣾⣿⣿⣿⣿⣾⣿⣷⡀⠓⠠⠤⣀⣀⡀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠘⣇⠀⠀⠀⣿⣠⡴⠟⡿⠁⠀⠀⠀⠀⠀⠀⣿⣿⡟⠁⣰⣿⣿⠁⣾⡟⢛⣻⣿⣿⣿⣿⣿⣿⣶⣧⣤⣀⣀⣤⣶⡄⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠹⣍⠢⢄⠸⡏⠀⡜⠀⠀⠀⣀⣠⡤⠤⠶⠿⠿⠷⠶⣿⣿⣇⡀⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠒⣉⣤⣤⣤⣘⡷⢤⣙⠹⣴⠁⣠⡶⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⢁⣴⡿⠿⠿⣿⣿⣿⣿⠖⠋⣩⠗⢚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢯⣅⠀⠀⠉⠉⠛⠛⠛⠛⣯⠁⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡜⢠⣞⣡⣤⣤⣄⣰⣟⠟⠁⠀⡞⠁⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡦⢄⣀⣀⣀⣀⣀⡸⢧⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⣾⣆⡉⠻⣿⣿⡿⠁⠀⠀⢠⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⣠⣾⡀⠳⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⢹⣿⣿⣶⣼⠟⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣤⣞⣋⣀⣷⣦⡈⠒⠒⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢣⠘⣿⣿⣿⠇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠙⠶⣄⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠉⠉⢁⡼⠈⠙⠓⠚⡇⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡘⣿⣿⠀⠀⠀⠀⠀⠀⡿⡆⠀⠀⠀⠀⡄⠀⠀⠀⠈⠉⠒⠦⠤⢄⣀⣀⢠⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⢀⣠⡴⠛⢠⣀⣀⣠⡾⢁⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⠈⣿⠀⠀⠀⠀⠀⠀⣷⠹⡀⠀⠀⠀⠹⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠛⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⣯⠉⠉⠙⠲⢦⣸⡉⢭⡥⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢀⡏⠀⠀⠀⠀⠀⠀⣧⠀⠹⣄⠀⠀⠀⠙⢏⠓⠲⠶⠖⠒⢺⣯⡁⠀⠀⠀⠀⠘⡘⡄⠀⠀⠀⠀⠑⣄⠀⣼⠀⠀⠀⠀⠀⠈⠻⣄⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⡼⠁⠀⠀⠀⠀⠀⠀⢹⠀⠀⠈⠳⣄⡀⠀⠈⠓⢄⠀⠀⠀⠘⣷⠘⢦⣀⠀⠀⠀⡇⠱⡀⠀⠀⠀⠀⠈⢧⡟⠀⠸⡒⠢⣄⠀⠀⢸⡄⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠤⠊⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠉⠉⠒⠒⠚⠁⠀⠀⠀⢸⣀⡀⠬⠛⠷⣶⣈⣀⣧⠀⠀⠀⠀⠀⠘⡇⠀⠀⠘⣆⠘⣿⣄⢸⠃⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⢰⡋⠁⠀⠀⣠⣾⠀⠀⠀⡄⠀⠀⢧⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⣹⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠘⡆⣿⣿⡋⢰⡁⢀⠔⢉⡉⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢂⡙⠶⠶⠿⢿⠃⡄⢸⠀⢧⠀⠀⠈⣷⣤⡄⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⢀⠀⢸⠀⠀⠀⠀⠀⠀⡇⠀⢠⠀⠀⣧⡇⠈⠻⣆⠑⢋⣠⠏⢻⠀⣇⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢶⡇⢸⡆⠱⡇⠀⠈⢦⠀⠀⠹⡌⠙⠾⢔⣠⠀⢻⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⣠⣶⣿⠆⣸⠀⠀⠀⠀⠀⡸⠁⠀⡜⠀⢠⡏⠉⠛⠲⢮⣭⣉⠀⢠⠾⠶⣦⡈⢢⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡠⠔⢉⣡⣤⣤⠿⣦⣧⠀⠀⠈⣷⣄⠀⠹⣄⠀⠀⠈⠑⠺⡇⠀⠀⣸⠃⠨⣭⣥⠶⣺⠿⠟⠁⢀⡏⠀⠀⡼⣠⠞⢁⡠⠞⠀⢀⡞⠀⠀⠀⠀⠀⠈⠙⠳⣦⣤⣤⣀⡇⢸⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠔⣡⡴⠞⠋⠉⠀⠀⠠⢌⢻⠀⠀⠀⠈⢯⠉⠁⠈⠁⣀⣤⠤⣰⠀⠀⣴⠃⠀⠀⠉⠉⠛⠁⠀⠀⠀⡼⠁⢀⡼⠋⠁⠙⠥⣤⡤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡙⢁⡞⠀⠀⠀⠀
⠀⠀⢀⠔⣡⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⠀⠰⡀⠈⠳⣿⣶⣶⣶⣶⠿⠓⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣤⠶⠋⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠑⢄⠀⠀⠀
⠀⣀⠎⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⣄⠙⣦⣄⣀⣩⠶⠁⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⣀⡤⣶⠏⠀⢀⡤⠖⣺⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡈⢆⠀⠀
⡎⣴⠖⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠉⢸⣿⣿⣦⣀⣀⠀⠀⠀⣀⣀⣀⣠⡤⠴⠚⡉⠁⢰⠁⠀⢠⠏⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠈⢆⠀
⠣⡉⠳⢦⣌⠁⠲⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⢌⣿⣿⣿⣿⣿⣿⣿⣿⣝⠋⠁⠀⠀⡀⠊⢀⡴⢻⡀⠀⣇⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠘⡄
⠀⠀⠁⠢⡙⢦⣈⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣧⣀⣑⣦⠀⠉⢀⣴⠋⠀⠀⠙⠦⠏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣧⠸
⠀⠀⠀⠀⠈⠢⡈⠳⢦⣄⡉⠐⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡁⠐⢯⡉⠉⣹⠟⠁⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⣸⠆
⠀⠀⠀⠀⠀⠀⠀⠁⠢⢌⡉⠛⠶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠉⠑⠂⠄⠀⣀⣀⣩⡷⠿⣦⠞⠁⠀⠄⠒⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⣡⡴⠋⡔
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠠⠤⠈⣉⣉⣉⠛⠛⠛⠛⠛⠛⠦⣤⠏⡠⠤⠰⡀⠳⢤⣄⣈⡑⠒⠤⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠾⠖⢋⡡⠔⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠀⠊⠀⠀⠀⠈⠐⠢⠤⢉⣙⠛⠛⠒⠶⠶⠶⢤⣤⣤⣤⣤⣤⣀⣀⣀⣀⣠⣤⣤⠤⠤⠤⠶⠖⠚⠛⣉⡡⠤⠔⠊⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠐⠒⠀⠀⠀⠀⠤⠤⠤⠤⠤⠤⠤⠤⠄⠀⠀⠒⠓⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ """

ganyu2 = """ 
⠀⠀⠀⠁⠀⠀⠀⠀⢀⠀⠀⠀⡀⠀⢠⠞⠀⠀⢀⡴⠋⠀⢠⠀⠀⠀⡀⠀⠀⠈⠛⣆⠀⠀⠀⢻⠀⠀⠀⢀⡀⠈⠀⡀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠈⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠄⠀⠀⠠⠀⠀⠀⠤⠀⠀⠀⡞⠀⠀⢠⠟⠀⠠⠀⠀⠀⠤⠀⠀⠠⠀⠀⠀⠙⣦⠀⠀⣸⠀⠀⠄⠀⠀⠠⠀⠀⠀⠄⠀⠀⠤⠀⠀⠀⠄⠀⠀⠠⠀⠀⠀⠄⠀⠀⠠⠀⠀
⠀⠠⠀⠀⠀⠄⠀⠀⠰⠀⠀⠀⠄⠀⢧⠀⢀⠀⠀⠄⠀⠀⠴⠀⠀⠀⠄⠀⠀⠠⠀⠀⢻⠀⢀⡿⠀⠀⠀⠠⠆⠀⠀⠤⠀⠀⠠⠄⠀⠀⠄⠀⠀⠀⠀⠀⠀⠄⠀⠀⠠⠀⠀⠀⠄
⠂⠀⠀⠂⠀⠀⠐⠀⠀⠀⠒⠀⠀⠀⠘⣆⣾⠀⠀⠀⠐⠀⠀⠀⠒⠀⠀⠐⠀⠀⠀⠀⣾⣠⠟⠁⠀⠀⠒⠀⠀⠐⠀⠀⠀⠂⠀⠀⠒⠀⠀⠀⠂⠀⠀⠐⠀⠀⠀⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠂⠀⠀⠐⠀⠀⠀⠂⠀⠀⠘⢻⡀⠀⠂⠀⠀⠒⢀⣀⣤⣤⣤⣤⣤⣀⣼⣿⣥⣤⣤⣤⣤⣄⣠⣤⣶⡿⠿⠟⣻⡛⢲⣄⠀⠂⠀⠀⠐⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠁⠀⠀⠈⠁⠀⠀⠉⠀⠀⠈⠁⢀⡀⠑⠀⢀⣤⡴⠞⠋⠉⠉⠀⠀⠀⠘⠛⠁⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⢶⣾⣿⣿⠁⣾⣿⣷⡄⠀⠁⠀⠀⠈⠀⠀⠀⠁⠀⠀⠀⠀⠀
⡀⠈⠀⡀⠀⠁⠀⠀⣈⣀⣀⣤⣤⣤⡀⠉⠀⢠⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⢠⡀⠀⣤⣶⣦⣄⠀⠀⠀⠉⠻⣤⣿⣿⣿⣿⡄⠀⠈⠀⢀⠀⠁⠀⡀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⣠⣶⣿⣿⣷⣾⣿⣿⣿⣿⣷⡶⠋⠀⠀⠀⠀⢀⣴⣿⡿⠛⠀⠠⡟⠀⠀⠀⠀⠀⠱⣄⠀⠈⠉⠙⠛⠢⣄⠀⠀⠀⠙⢿⣿⣿⣷⠀⢠⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⠿⠋⣹⣽⣯⣿⣽⠏⠀⠀⠀⠀⠀⢠⡾⠛⠁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠈⠻⡲⣄⠀⠀⠉⠻⣿⡀⠀⠀⠠⠀⠀⠀⠄⠀⠀⠠⠀⠀
⢷⡀⠀⣾⣿⡿⠋⣀⣠⢈⠉⠙⠿⡿⠃⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⢰⠀⠀⠀⣧⠀⠀⠀⢠⡀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠘⢮⣣⡀⠀⠲⣤⣍⡓⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣴⣿⠏⢠⣾⣿⣿⣿⣷⣶⣾⠃⠀⠀⠀⠀⠀⢰⠋⠀⠀⠀⠀⢸⠀⠀⠀⢸⡄⠀⠀⠀⠻⡀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠙⣿⡀⠀⠹⣎⠉⠓⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢹⣯⣠⣿⣿⣿⣅⢉⣿⣿⡏⠀⠀⠀⠀⠀⠠⠏⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠻⣆⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠘⣷⠀⠀⠙⣷⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⢸⣇⠀⠀⡀⠀⠘⢦⡀⠀⠀⠙⢷⢤⣀⠀⠀⠀⠀⠀⠈⠉⢉⡉⠹⣇⠀⠀⠈⣷⡀⠀⠀⣿⢷⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⡀⠀⠀⢸⠀⠀⠀⢸⢿⠀⠀⢧⠀⠀⠀⠉⠳⢦⣄⣈⡳⢮⣉⡓⠲⠶⡶⠚⠉⠁⠀⠀⢹⡆⠀⠀⠘⢧⠀⠀⢸⡎⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⠀⠀⠀⡏⠈⣇⠀⠸⣆⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠉⡗⡦⣹⣦⣀⣀⠀⠀⠘⣇⠀⠀⠀⠈⠳⡄⢸⡇⡷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠸⡄⠀⠈⣇⠀⠀⡇⠀⢘⣶⡾⢿⡇⠀⠀⠀⠀⠈⡇⠀⠀⠀⢠⣧⠇⠀⠀⠉⠳⠦⣀⡀⣿⠀⠀⠀⠀⠀⠈⡿⠁⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢿⠁⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⣿⠤⢾⡗⠋⠉⠉⠳⣄⢻⣦⣀⠀⠀⠀⢿⠀⠀⠀⣾⠟⠀⠀⠀⢀⣰⣃⣀⠉⣿⠀⠀⠀⢀⡇⠀⠁⠀⠀⠀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⢃⡾⠀⠀⢸⡃⠀⠀⠀⠀⠸⡄⠀⣿⡆⢸⡇⠀⠀⠀⠀⠀⠉⠛⢮⡳⢦⣀⢸⠀⠀⣼⠏⢴⣶⣻⣯⣿⣿⡿⠽⠁⡿⠀⠀⠀⣸⢀⣀⣀⣀⡤⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡿⠁⡼⠁⠀⠀⡼⡇⠀⠀⠀⠀⠀⢻⡀⣿⢹⣜⡇⢀⠤⠖⣺⣿⣅⣀⠀⠉⠓⠂⣾⠀⡼⠃⠀⠀⠉⠉⠀⠀⠀⠀⠀⢸⡇⠀⠀⣰⠇⠀⠀⠙⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣇⡼⠁⠀⢀⡼⠁⢣⠀⠀⢰⡄⠀⠀⢳⣿⠀⣹⣷⣶⣾⣯⡷⠾⠟⠃⠀⠀⠀⢀⣯⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⢀⡼⠃⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⠁⢀⣴⠟⠁⠀⠘⡆⠀⠈⣷⠀⠀⠀⠻⣇⠋⠛⠛⠉⠀⠀⠀⠀⠀⠀⣀⣠⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣃⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡷⠚⠋⢷⠀⠀⠀⠀⠹⣆⠀⠈⣧⡀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠛⠋⠁⢸⣆⠀⠀⠀⠀⠀⣿⣦⠀⠀⣿⡆⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡀⠀⠀⠀⠀⠙⢦⡀⠘⣿⢦⣄⠀⠀⠈⠓⠦⢤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⡇⠀⠀⠀⠀⡿⠘⡆⠀⣿⠇⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠙⠦⣌⣳⣌⠛⠲⣤⠤⠴⠒⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡇⣿⠀⠀⠀⣸⠇⠀⣧⣠⠏⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⣸⠃⠀⣠⡦⢦⡀⠀⠀⠀⠀⠀⠙⠳⠦⠜⣦⡀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⣰⡏⢀⣠⠾⠋⠀⠀⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⠀⠀⣰⣟⣤⠞⢻⡄⠘⣟⢦⣀⠀⠀⠀⠀⡀⠀⠀⠈⠛⠷⣤⣀⣀⣀⡄⠀⠀⠀⠀⠀⠀⢀⣠⠤⠶⠦⣤⣴⠾⣋⠀⣠⣴⢿⠞⠋⢛⣳⠢⣄⡚⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠛⠷⢾⣿⣯⡤⠄⠈⠳⣤⣻⣄⠉⢛⣦⣤⣠⣟⠶⢤⣤⣀⣀⣠⡬⠟⠿⢦⣤⣤⣤⣤⣴⡾⠋⠁⠀⣀⣤⡈⢳⡄⠈⠛⠶⢤⣈⣙⠳⣌⣿⠆⠨⢷⡀⠀⠀⠀⣾
⠀⠀⠀⠀⠀⢀⣴⠾⠛⣻⣿⡀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣦⣙⡈⡆⠈⠙⣷⡄⠀⠀⣰⠿⣿⣿⣿⠏⣀⠀⠀⠀⠉⠉⠉⠛⣷⡄⠀⠀⠀⠀⠉⣹⣿⠋⠀⣾⡀⡇⠀⠀⠠⠟
⠀⠀⠀⠀⠀⢸⣿⠴⠚⠁⢸⣿⣿⣿⣿⠋⠁⢀⣩⣤⣤⣬⠉⣹⣿⡇⣿⡄⠀⠈⣿⡀⣴⠋⠀⠈⣿⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⠟⠀⠀⠀⣠⡾⠟⠁⠀⢰⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢨⣿⣿⣿⣿⣄⠀⠀⠉⠉⠉⣿⢠⣿⣿⣱⣷⠃⠀⠀⢸⡿⠁⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⣴⡿⠁⠀⠀⢠⣾⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⢀⣾⣿⣹⣿⣿⣿⣿⣖⣶⣏⠀⣧⡾⢋⣿⡿⠃⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⣻⣀⠀⠀⠀⠰⠤⠤⣄⣺⡇⠀⠀⣼⣟⠀⢀⣤⣤⣾⡿⠀⡇⡆⠀⠀⠀⠀ """

def baguting():
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissors wins \n")

    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        # Take the input from user
        choice = int(input("Enter your choice: "))

        # Looping until user enters valid input
        while choice > 3 or choice < 1:
            choice = int(input('Enter a valid choice please ☺: '))

        # Initialize value of choice_name variable corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        # Print user choice
        print('User choice is:', choice_name)
        print("Now it's Computer's Turn...")

        # Computer chooses randomly any number among 1, 2, and 3
        comp_choice = random.randint(1, 3)

        # Initialize value of comp_choice_name variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print("Computer choice is:", comp_choice_name)
        print(choice_name, 'vs', comp_choice_name)

        # Determine the winner
        if choice == comp_choice:
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = 'Paper'
        elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
            result = 'Rock'
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = 'Scissors'

        # Print the result
        if result == "DRAW":
            print("<== It's a tie! ==>")
        elif result == choice_name:
            print("<== User wins! ==>")
        else:
            print("<== Computer wins! ==>")

        # Ask if the user wants to play again
        print("Do you want to play again? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break

    # After coming out of the while loop, print thanks for playing
    print("Thanks for playing!")
    
def jokes():
    joke1 = pyjokes.get_joke(language='en', category= 'all')  
    #display the joke
    engine.say(joke1)
    print(joke1)
    engine.runAndWait()

def putarkan ():
    while True:
        inputehe = input("\033[1;37;44mFijinCLI>\033[0m ").strip().split()
        
        if not inputehe:
            continue
        
        ceemde = inputehe[0]
        ehe = inputehe[1:]
        
        if ceemde == "mkdir" and ehe:
            mkdir(ehe[0])
        elif ceemde == "ls":
            ls()
        elif ceemde == "pwd":
            pwd()
        elif ceemde == "cd" and ehe:
            cd(ehe[0])
        elif ceemde == "rm" and ehe:
            rm(ehe[0])
        elif ceemde == "touch" and ehe:
            touch(ehe[0])
        elif ceemde == "rmdir" and ehe:
            rmdir(ehe[0])
        elif ceemde == "cp" and len(ehe) == 2:
            cp(ehe[0], ehe[1])
        elif ceemde == "mv" and len(ehe) == 2:
            mv(ehe[0], ehe[1])
        elif ceemde == "help":
            helepp()
        elif ceemde == "clear":
            clear()
        elif ceemde == "ganyu":
            print(ganyu)
        elif ceemde == "exit":
            print(ganyu)
            print("Exiting...")
            print("Babay...")
            sys.exit(0)
        elif ceemde == "art":
            art()
        elif ceemde == "janken":
            baguting()
        elif ceemde == "jokes":
            jokes()
        elif ceemde == "frieren":
            frieren()
            
if __name__ == "__main__":
    try:
        print("Running...")
        time.sleep(2)
        print(ganyu2)
        putarkan()
    except KeyboardInterrupt:
        print("\nExiting...")
        print("Babay...")
        print(ganyu)
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Exiting...")
        print("Babay...")
        sys.exit(1)
