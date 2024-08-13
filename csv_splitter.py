import pandas as pd
import os
import math
import time

class CSVSplitter:
    def __init__(self, file_name, split_size=10000):
        """
        CSVSplitter 초기화 메서드
        :param file_name: 분할할 CSV 파일의 이름
        :param split_size: 각 분할 파일에 포함될 행 수, 기본값은 10,000
        """
        self.file_name = file_name
        self.split_size = split_size
        self.current_directory = os.getcwd()
        self.file_path = os.path.join(self.current_directory, f"{self.file_name}.csv")
        self.validate_inputs()

    def validate_inputs(self):
        """
        입력 값의 유효성을 검사
        """
        if not os.path.exists(self.file_path):
            print(f"Error: '{self.file_path}' 파일이 존재하지 않습니다.")
            time.sleep(5)
            raise FileNotFoundError(f"Error: '{self.file_path}' 파일이 존재하지 않습니다.")
        
        if not self.file_path.lower().endswith('.csv'):
            print("Error: CSV 파일만 가능합니다.")
            time.sleep(5)
            raise ValueError("Error: CSV 파일만 가능합니다.")
        
        if os.path.getsize(self.file_path) == 0:
            print("Error: 파일 크기가 0KB입니다.")
            time.sleep(5)
            raise ValueError("Error: 파일 크기가 0KB입니다.")
        
    def split_csv(self):
        """
        CSV 파일을 분할하여 여러 파일로 저장
        """
        df = pd.read_csv(self.file_path)
        total_rows = len(df)
        
        if total_rows == 0:
            print("Error: CSV 파일에 데이터가 없습니다.")
            time.sleep(5)
            raise ValueError("Error: CSV 파일에 데이터가 없습니다.")

        num_splits = math.ceil(total_rows / self.split_size)

        base_name = os.path.splitext(os.path.basename(self.file_path))[0]
        for i in range(num_splits):
            start_row = i * self.split_size
            end_row = min((i + 1) * self.split_size, total_rows)
            split_df = df.iloc[start_row:end_row]
            
            split_file_name = os.path.join(self.current_directory, f"{base_name}_{i + 1}.csv")
            split_df.to_csv(split_file_name, index=False)
            print(f"파일 저장됨: {split_file_name}")
        
        print(f"CSV 파일들이 분할되어 {self.current_directory} 폴더에 저장되었습니다.")
        time.sleep(5)  # 5초 대기

def main():
    """
    메인 함수: 사용자 입력을 받아 CSVSplitter 인스턴스를 생성하고 분할 작업을 수행
    """
    file_name = input("분할할 CSV 파일의 이름을 입력하세요 (확장자 제외): ").strip()

    while True:
        split_size_input = input("파일을 나눌 행 수를 입력하세요 (기본값: 10,000): ").strip()
        if not split_size_input:  # 입력이 없으면 기본값 사용
            split_size = 10000
            break
        try:
            split_size = int(split_size_input)
            if split_size <= 0:
                raise ValueError("Error: 분할 크기는 0보다 큰 양수여야 합니다.")
            break
        except ValueError:
            print("유효한 숫자를 입력하세요.")
    
    try:
        splitter = CSVSplitter(file_name, split_size)
        splitter.split_csv()
    except Exception as e:
        print(str(e))
        time.sleep(5)

if __name__ == "__main__":
    main()
