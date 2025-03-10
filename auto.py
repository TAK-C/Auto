import pyautogui
import time
import keyboard
import os  # 디렉토리 파일 수 확인을 위해 추가

# 실수로 프로그램을 종료할 수 있도록 안전장치 설정
pyautogui.FAILSAFE = True

# 미리 정의된 위치 목록
PREDEFINED_POSITIONS = [
    pyautogui.Point(x=1552, y=394),
    pyautogui.Point(x=1552, y=416),
    pyautogui.Point(x=1553, y=442),
    pyautogui.Point(x=1557, y=467),
    pyautogui.Point(x=1556, y=489),
    pyautogui.Point(x=1554, y=509),
    pyautogui.Point(x=1555, y=534),
    pyautogui.Point(x=1558, y=557),
    pyautogui.Point(x=1558, y=580),
    pyautogui.Point(x=1556, y=606),
    pyautogui.Point(x=1555, y=629),
    pyautogui.Point(x=1556, y=652),
    pyautogui.Point(x=1560, y=679),
    pyautogui.Point(x=1556, y=700),
    pyautogui.Point(x=1556, y=723),
    pyautogui.Point(x=1556, y=749),
    pyautogui.Point(x=1558, y=773),
    pyautogui.Point(x=1556, y=796),
    pyautogui.Point(x=1557, y=819),
    pyautogui.Point(x=1559, y=842),
    pyautogui.Point(x=1557, y=869),
    pyautogui.Point(x=1557, y=890),
    pyautogui.Point(x=1556, y=915),
    pyautogui.Point(x=1558, y=939),
    pyautogui.Point(x=1555, y=961),
    pyautogui.Point(x=1558, y=986),
    pyautogui.Point(x=1556, y=1013),
    pyautogui.Point(x=1557, y=1034),
    pyautogui.Point(x=1557, y=1060),
    pyautogui.Point(x=1559, y=1083),
    pyautogui.Point(x=1558, y=1105),
    pyautogui.Point(x=1559, y=1129),
    pyautogui.Point(x=1558, y=1153),
    pyautogui.Point(x=1557, y=1178),
    pyautogui.Point(x=1555, y=1201),
    pyautogui.Point(x=1556, y=1225),
    pyautogui.Point(x=1556, y=1248),
    pyautogui.Point(x=1555, y=1274),
    pyautogui.Point(x=1557, y=1297),
    pyautogui.Point(x=1557, y=1320),
    pyautogui.Point(x=1557, y=1344),
    pyautogui.Point(x=1556, y=1371),
    pyautogui.Point(x=1556, y=1392),
    pyautogui.Point(x=1556, y=1415),
    pyautogui.Point(x=1559, y=1438),
    pyautogui.Point(x=1562, y=1461),
    pyautogui.Point(x=1557, y=1487),
    pyautogui.Point(x=1558, y=1511),
    pyautogui.Point(x=1557, y=1534),
    pyautogui.Point(x=1561, y=1558),
    pyautogui.Point(x=1531, y=1692)
]

def get_file_count(directory):
    """지정된 디렉토리의 파일 수를 반환합니다."""
    try:
        return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    except Exception as e:
        print(f"경고: {directory} 디렉토리를 읽을 수 없습니다. ({e})")
        return 0

def get_mouse_positions(section_name):
    positions = []
    print(f"\n{section_name} 위치를 저장합니다.")
    print("마우스 위치를 저장하려면 's'키를, 완료하려면 'q'키를 누르세요.")
    
    while True:
        time.sleep(0.1)  # 키 입력 감지를 위한 딜레이 추가
        
        if keyboard.is_pressed('s'):
            current_pos = pyautogui.position()
            positions.append(current_pos)
            print(f"위치 저장됨: {current_pos}")
            while keyboard.is_pressed('s'):  # 키가 떼질 때까지 대기
                time.sleep(0.1)
        
        elif keyboard.is_pressed('q'):
            while keyboard.is_pressed('q'):  # 키가 떼질 때까지 대기
                time.sleep(0.1)
            break
    
    return positions

def click_positions_manual(major_positions, minor_positions):
    last_position = pyautogui.position()  # 시작 위치 저장
    major_index = 0
    minor_index = -1  # -1로 시작하여 첫 클릭에서 0이 되도록 함
    file_count = 0  # 파일 카운터 추가
    print("\n클릭을 시작합니다. (종료하려면 ESC)")
      
    try:
        while True:
            if keyboard.is_pressed('esc'):  # ESC 키 감지
                print("\nESC 키 입력: 프로그램을 종료합니다.")
                return  # 함수 종료
                
            if keyboard.is_pressed('space'):
                while keyboard.is_pressed('space'):  # 키가 떼질 때까지 대기
                    time.sleep(0.1)
                
                # 현재 위치 클릭
                if minor_index == -1:
                    print(f"\n주요 위치 클릭: {major_positions[major_index]}")
                    pyautogui.click(major_positions[major_index].x, major_positions[major_index].y)
                    
                    # 마지막 주요 위치였다면 처음으로 돌아가기
                    if major_index == len(major_positions) - 1:
                        major_index = 0
                        print(f"\n시작 위치로 복귀: {last_position}")
                        pyautogui.moveTo(last_position.x, last_position.y)
                        continue
                    else:
                        minor_index = 0  # 다음은 첫 번째 보조 위치부터 시작
                
                else:
                    print(f"보조 위치 클릭: {minor_positions[minor_index]}")
                    pyautogui.click(minor_positions[minor_index].x, minor_positions[minor_index].y)
                    
                    # 인덱스 업데이트
                    minor_index += 1
                    if minor_index >= len(minor_positions):
                        file_count += 1  # 보조 위치 사이클 완료시 카운터 증가
                        print(f"\n현재까지 완료된 파일 수: {file_count}")
                        minor_index = -1  # 다음 주요 위치로 이동
                        major_index += 1
                
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

def click_positions_auto(major_positions, minor_positions, delay, final_delay, watch_directory, loop_count=None):
    last_position = pyautogui.position()  # 시작 위치 저장
    major_index = 0
    minor_index = -1
    current_loop = 0
    file_count = 0  # 파일 카운터 추가
    original_delay = delay  # 원래 딜레이 값 저장
    current_delay = delay  # 현재 딜레이 값
    print("\n클릭을 시작합니다. (종료하려면 ESC)")
      
    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("\nESC 키 입력: 프로그램을 종료합니다.")
                return
            
            if minor_index == -1:
                # print(f"\n주요 위치 클릭: {major_positions[major_index]}")
                pyautogui.click(major_positions[major_index].x, major_positions[major_index].y)
                initial_file_count = get_file_count(watch_directory)
                
                if major_index == len(major_positions) - 1:
                    major_index = 0
                    current_loop += 1
                    
                    if loop_count and current_loop >= loop_count:
                        print(f"\n설정된 반복 횟수({loop_count}회)가 완료되었습니다.")
                        return
                        
                    print(f"\n시작 위치로 복귀: {last_position} (현재 {current_loop}회 완료)")
                    pyautogui.moveTo(last_position.x, last_position.y)
                    time.sleep(final_delay)
                    continue
                else:
                    minor_index = 0
            
            else:
                # print(f"보조 위치 클릭: {minor_positions[minor_index]}")
                pyautogui.click(minor_positions[minor_index].x, minor_positions[minor_index].y)
                
                minor_index += 1
                if minor_index >= len(minor_positions):
                    final_file_count = get_file_count(watch_directory)
                    if final_file_count == initial_file_count:
                        # 파일 수 변화가 없을 경우 딜레이 증가
                        current_delay += 1.0
                        print(f"\n파일 수 변화 없음. 딜레이를 {current_delay}초로 증가시킵니다.")
                        minor_index = -1
                    else:
                        # 파일 수 변화가 있을 경우 원래 딜레이로 복귀
                        if current_delay != original_delay:
                            current_delay = original_delay
                            print(f"\n파일 수 변화 감지. 딜레이를 원래값({original_delay}초)으로 복귀합니다.")
                        file_count += 1
                        print(f"\n현재까지 완료된 파일 수: {file_count}")
                        minor_index = -1
                        major_index += 1
            
            time.sleep(current_delay)
                
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    print("프로그램을 시작합니다.")
    
    try:
        # 모드 선택
        mode = input("모드를 선택하세요 (1: 수동, 2: 자동): ").strip()
        
        if mode == "1":  # 수동 모드
            print("\n수동 모드를 시작합니다.")
            print("스페이스바를 눌러 다음 위치로 이동합니다.")
            
            # 주요 위치들 저장
            major_positions = get_mouse_positions("주요(큰 범위)")
            # 보조 위치들 저장
            minor_positions = get_mouse_positions("보조(작은 범위)")
            
            if major_positions and minor_positions:
                print(f"\n총 {len(major_positions)}개의 주요 위치와 {len(minor_positions)}개의 보조 위치가 저장되었습니다.")
                click_positions_manual(major_positions, minor_positions)
            else:
                print("저장된 위치가 없습니다.")
                
        elif mode == "2":  # 자동 모드
            print("\n자동 모드를 시작합니다.")
            
            delay = float(input("일반 클릭 사이의 딜레이를 초 단위로 입력하세요 (예: 0.5): "))
            final_delay = float(input("마지막 주요 위치 클릭 후의 딜레이를 초 단위로 입력하세요 (예: 2.0): "))
            loop_input = input("전체 반복 횟수를 입력하세요 (무한반복은 엔터): ")
            loop_count = int(loop_input) if loop_input.strip() else None
            
            watch_directory = input("감시할 디렉토리 경로를 입력하세요: ")
            if not os.path.exists(watch_directory):
                print("경고: 지정된 디렉토리가 존재하지 않습니다.")
                exit(1)
            
            use_predefined = input("미리 정의된 위치를 사용하시겠습니까? (y/n): ").lower().strip()
            
            if use_predefined == 'y':
                major_positions = PREDEFINED_POSITIONS
                print(f"\n미리 정의된 {len(major_positions)}개의 주요 위치를 사용합니다.")
                minor_positions = get_mouse_positions("보조(작은 범위)")
            else:
                major_positions = get_mouse_positions("주요(큰 범위)")
                minor_positions = get_mouse_positions("보조(작은 범위)")
            
            if major_positions and minor_positions:
                print(f"\n총 {len(major_positions)}개의 주요 위치와 {len(minor_positions)}개의 보조 위치가 저장되었습니다.")
                click_positions_auto(major_positions, minor_positions, delay, final_delay, watch_directory, loop_count)
            else:
                print("저장된 위치가 없습니다.")
        
        else:
            print("잘못된 모드를 선택했습니다.")
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")