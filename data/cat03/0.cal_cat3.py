import os
import json

# 1. 폴더 내의 json 파일을 번호 붙여 리스팅
def list_json_files():
    files = [f for f in os.listdir() if f.endswith('.json')]
    if not files:
        print("No JSON files found in the current directory.")
        return []
    
    print()
    for idx, file in enumerate(files):
        print(f"{idx + 1}: {file}")
    return files

# 2. json 파일을 가공하는 함수
def process_json_data(data):
    # 각 데이터의 flow_value를 1000으로 나누고 int로 변환하여 flow_valueB로 추가
    for item in data['data']:
        item['flow_valueB'] = int(item['flow_value'] / 1000)

    # to_cat10_cd가 "1"로 시작하는 경우에 대해 처리
    result = {}
    
    for item in data['data']:
        to_cat3_cd = item['to_cat3_cd']
        from_cat3_cd = item['fr_cat3_cd']
        
        # to_cat3_cd가 "3"으로 시작하고 from_cat3_cd도 "3"으로 시작하는 데이터 필터링
        if to_cat3_cd.startswith("3") and from_cat3_cd.startswith("3"):
            if to_cat3_cd not in result:
                result[to_cat3_cd] = 0
            result[to_cat3_cd] += item['flow_valueB']
    
    return result

# 3. 프로그램 시작 함수
def main():
    json_files = list_json_files()
    
    if not json_files:
        return
    
# 4. 사용자로부터 파일 선택
    try:

        print()        
        file_num = int(input("처리할 JSON 파일의 번호를 입력하세요: ")) - 1
        if file_num < 0 or file_num >= len(json_files):
            print("잘못된 번호입니다. 프로그램을 종료합니다.")
            return
    except ValueError:
        print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")
        return
    
# 5. 선택한 JSON 파일 읽기
    selected_file = json_files[file_num]
    with open(selected_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
# 6. 데이터를 가공
    processed_data = process_json_data(data)
    
# 7. 가공된 결과 라인 생성
    result_lines = []
    for to_cat3_cd, total_flow_valueB in processed_data.items():
        # 첫 번째로 to_cat3_cd에 ">FIN;"을 더한 결과
        line1 = f"{to_cat3_cd}>FIN;{total_flow_valueB}"
        result_lines.append(line1)
        
    result_lines.append("")
    for to_cat3_cd, total_flow_valueB in processed_data.items():
        # 두 번째로 "INIT>" + to_cat3_cd 형식으로 결과
        line2 = f"INIT>{to_cat3_cd};{total_flow_valueB}"
        result_lines.append(line2)

    result_lines.append("")
    
# 8. 원 데이터에서 flow_cat3_id와 flow_valueB 결합하여 결과 파일에 추가
    for item in data['data']:
        flow_cat3_id = item['flow_cat10_id']
        flow_valueB = item['flow_valueB']
        combined = f"{flow_cat3_id};{flow_valueB}"
        result_lines.append(combined)
        
        
# 9. 가공된 결과 저장할 파일 이름 결정
    result_file_name = selected_file.replace('.json', '.txt')



#10. 파일 이름에서 YR QTR추출하기
    import re
    yrqtr = re.search(r'results-(\d{4}Q\d)', result_file_name).group(1);
    
    # 추출한 yrqtr을 result_lines 맨 앞에 추가
    result_lines.insert(0, "")    
    result_lines.insert(0, f"YRQTR; {yrqtr}")    

    print(yrqtr)




# 10. 가공된 결과 저장 (괄호 없이 텍스트 형식, 빈 줄 제거)
    with open(result_file_name, 'w', encoding='utf-8') as f:
        f.write("\n".join(result_lines))
    
    print(f"가공된 결과가 '{result_file_name}'에 저장되었습니다.")

if __name__ == "__main__":
    main()
