import pandas as pd #pandas 라이브로리 import
import re  # re 모듈을 import

# CSV 파일 경로
Symbol_Atomic_Weight = '/Users/judongcheol/Library/Mobile Documents/com~apple~CloudDocs/대학교/2학년 2학기/프로그래밍 2/코딩 파일/dongcheolju_Calculator_Quiz/Symbol,Atomic Weight.csv'

# CSV 파일 데이터 프레임에 읽기
df = pd.read_csv(Symbol_Atomic_Weight)

# 화학식 입력 받기
chemical_formula = input("화학식을 입력하세요 : ")

# 화학식을 원소와 개수로 분리
elements = re.findall(r'([A-Z][a-z]*)(\d*)', chemical_formula)

# 원자량 계산
total_atomic_mass = 0.0
for element, count in elements:
    element_data = df[df['Symbol'] == element]
    if not element_data.empty:
        atomic_mass = element_data.iloc[0]['AtomicMass']
        count = int(count) if count else 1  # 정수로 변환, 기본값은 1
        atomic_mass = float(atomic_mass)  # 원자량을 숫자로 변환
        atomic_mass *= count
        total_atomic_mass += atomic_mass
    else:
        print(f"{element}를 찾을 수 없습니다.")

# 결과 출력
print(f"화학식: {chemical_formula}")
print(f"총 원자량: {total_atomic_mass} g/mol")
