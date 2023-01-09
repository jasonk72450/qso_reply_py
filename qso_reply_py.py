import os
import random
import sys


def print_and_write_file(_id, content):
    print(f"\nProtocol {_id}:\n")
    print(content)


def generate_all():
    other_call = input("Callsign to reply to: ").upper()
    rst = input("Enter their RST: ")
    other_name = input("Name of contact: ").upper()
    wx = input("Weather: ").upper()
    temperature = input("Enter the temperature: ")

    text1 = protocol_1(other_call, rst, other_name)
    print_and_write_file(1, text1)

    text2 = protocol_2(other_call, wx, temperature)
    print_and_write_file(2, text2)

    text3 = protocol_3(other_call)
    print_and_write_file(3, text3)

    text4 = protocol_4(other_call)
    print_and_write_file(4, text4)

    text5 = protocol_5(other_call, other_name)
    print_and_write_file(5, text5)


def protocol_1(other_call, rst, other_name):
    return f"""
{other_call} DE {my_call}
GM/GA/GE ES TNX FER RPRT
UR RST {rst} {rst}
QTH PARAGOULD, AR PARAGOULD, AR
NAME {my_name} {my_name}
OK HW? <AR>
{other_call} DE {my_call} <KN>
    """.strip()


def protocol_2(other_call, wx, temperature):
    return f"""
{other_call} DE {my_call}
OK FB ES TNX 
RIG ICOM 7300 ES PWR 100 W
ANT DIPOLE UP 50 FT
WX {wx} ES TEMP {temperature} F
OK HW? <AR>
{my_call} DE {other_call} <KN>
    """.strip()


def protocol_3(other_call):
    return f"""
{other_call} DE {my_call}
OK SOLID CPY
AGE 51 YRS
BEEN HAM FER 3 YRS
MY KEY VIBROPLEX
OK HW? <AR>  
{other_call} DE {my_call} <KN>
    """.strip()


def protocol_4(other_call):
    return f"""
{other_call} DE {my_call}
RR TU FER QSO
I AM FIREFIGHTER 22 YRS
HW? <AR> 
{other_call} DE {my_call} <KN>
    """.strip()


def protocol_5(other_call, other_name):
    return f"""
{other_call} DE {my_call}
OK {other_name} TNX FER FB QSO
ES HP CUAGN 73 <AR> 
{other_call} DE {my_call} <EE>
    """.strip()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        my_name = sys.argv[1]
        my_call = sys.argv[2]
    else:
        my_name = "JASON"
        my_call = "KE5JLN"
    generate_all()

