import pyautogui
import time
import keyboard

# 안전장치: 마우스 커서를 화면 구석에 이동하면 프로그램이 종료됨
pyautogui.FAILSAFE = True

# 딜레이 설정
delay = 11  # 각 클릭 사이의 딜레이 (초 단위)

def get_mouse_position(prompt):
    """
    마우스 위치를 's' 키로 설정받습니다.
    """
    print(f"{prompt} 위치를 설정하려면 's' 키를 누르세요.")
    
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('s'):
            position = pyautogui.position()
            print(f"{prompt} 위치 저장됨: {position}")
            while keyboard.is_pressed('s'):
                time.sleep(0.1)  # 키가 떼질 때까지 대기
            return position

def click_positions(positions, delay, repeat_count=None):
    """
    설정된 두 좌표를 반복적으로 클릭합니다.
    ESC 키를 누르면 프로그램이 종료됩니다.
    repeat_count가 설정되면 지정된 횟수만큼만 반복합니다.
    """
    print("\n반복 클릭을 시작합니다. (종료하려면 ESC 키를 누르세요)")
    
    try:
        index = 0
        click_count = 0
        while True:
            # ESC 키 감지 시 종료
            if keyboard.is_pressed('esc'):
                print("\nESC 키 입력: 프로그램을 종료합니다.")
                break

            # 반복 횟수 체크
            if repeat_count is not None:
                if click_count >= repeat_count * len(positions):
                    print(f"\n지정된 반복 횟수({repeat_count}회)가 완료되었습니다.")
                    break

            # 좌표 클릭
            x, y = positions[index]
            pyautogui.click(x, y)
            print(f"클릭 위치: {x}, {y}")

            # 다음 좌표로 이동
            index = (index + 1) % len(positions)
            click_count += 1
            
            # 딜레이
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("\n프로그램이 강제 종료되었습니다.")

if __name__ == "__main__":
    print("프로그램을 시작합니다.")
    
    # 딜레이 설정
    try:
        delay = float(input("클릭 사이의 딜레이를 초 단위로 입력하세요 (예: 11.0): "))
    except ValueError:
        print("올바른 숫자를 입력하지 않아 기본값 11초로 설정됩니다.")
        delay = 11.0
    
    # 반복 횟수 설정
    try:
        repeat_input = input("반복 횟수를 입력하세요 (무한반복은 엔터): ")
        repeat_count = int(repeat_input) if repeat_input.strip() else None
    except ValueError:
        print("올바른 숫자를 입력하지 않아 무한반복으로 설정됩니다.")
        repeat_count = None
    
    time.sleep(2)  # 준비 시간
    
    # 첫 번째와 두 번째 좌표 설정
    first_position = get_mouse_position("첫 번째")
    second_position = get_mouse_position("두 번째")
    
    # 설정된 좌표 저장
    positions = [first_position, second_position]
    
    print(f"\n설정된 좌표: {positions}")
    
    # 좌표를 반복 클릭
    click_positions(positions, delay, repeat_count)
