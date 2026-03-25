from typing import Dict, Union

class BMICalculator:
    def __init__(self, weight: float, height: float):
        """
        BMI 계산기 초기화
        :param weight: 체중 (kg)
        :param height: 신장 (cm)
        """
        self.weight = weight
        self.height = height / 100.0  # cm 단위의 신장을 m 단위로 변환

    def calculate_bmi(self) -> float:
        """
        BMI 수치 계산
        :return: 체중(kg) / 신장^2(m)
        """
        return self.weight / (self.height ** 2)

    def get_bmi_category(self) -> str:
        """
        계산된 BMI 수치를 바탕으로 비만도 범주 반환
        :return: 저체중, 정상, 과체중, 비만, 고도비만 중 하나 (문자열)
        """
        bmi = self.calculate_bmi()
        
        if bmi < 18.5:
            return "저체중"
        elif bmi < 23.0:
            return "정상"
        elif bmi < 25.0:
            return "과체중"
        elif bmi < 30.0:
            return "비만"
        else:
            return "고도비만"

    def get_result(self) -> Dict[str, Union[float, str]]:
        """
        최종 BMI 계산 결과 반환
        :return: 딕셔너리 형태의 결과값 (bmi 수치와 범주)
        """
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        
        return {
            "bmi": round(bmi, 2),
            "category": category
        }