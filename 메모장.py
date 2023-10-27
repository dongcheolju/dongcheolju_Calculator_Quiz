def calculate_molecular_weight(chemical_formula):
    # 화학식을 원소와 개수로 분리 / 매치된 부분을 모두 리스트로 취득하는 re 모듈의 findall 함수 사용
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', chemical_formula)
    # 초기 분자량 값 0 부여
    total_atomic_mass = 0.0

    #리스트에 있는 각 원소와 그 개수에 대해 반복
    for element, count in elements:
        #원소를 데이터 프레임에서 찾기
        element_data = df[df['Symbol'] == element] #df에서 해당 원소와 일치하는 행을 찾는 조건
        if not element_data.empty:                              #원소가 df에서 찾아졌는지 확인
            atomic_mass = element_data.iloc[0]['AtomicMass']    #원자량 가져오기
            count = int(count) if count else 1                  #count를 정수로 저장하되, 비어있을 경우 1로 저장(0일 경우 값이 0이 됨)
            atomic_mass = float(atomic_mass)                    #문자형을 부동소수 숫자형으로 전환
            atomic_mass = count * atomic_mass                   #원자량 곱하기 원소 개수
            total_atomic_mass = atomic_mass + total_atomic_mass #구해진 원자량을 총 분자량에 더하여 저장
        else:
            print(f"{element}를 찾을 수 없습니다.")

    return total_atomic_mass

def calculate_molecular_weight(chemical_formula):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', chemical_formula)
    total_atomic_mass = 0.0

    for element, count in elements:
        element_data = df[df['Symbol'] == element]
        if not element_data.empty:
            atomic_mass = element_data.iloc[0]['AtomicMass']
            count = int(count) if count else 1
            atomic_mass = float(atomic_mass)
            atomic_mass = count * atomic_mass
            total_atomic_mass = atomic_mass + total_atomic_mass
        else:
            print(f"{element}를 찾을 수 없습니다.")

    return total_atomic_mass
