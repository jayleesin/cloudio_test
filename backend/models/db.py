import pymysql
from pymysql import Error

class Database:
    def __init__(self, app=None):
        self.connection = None
        # 앱 인스턴스가 생성될 때 함께 전달되면 바로 초기화
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """App Factory 패턴을 위한 DB 초기화 메서드"""
        try:
            # config.py를 통해 로드된 app.config의 환경 변수 활용
            self.connection = pymysql.connect(
                host=app.config.get('DB_HOST'),
                port=app.config.get('DB_PORT'),
                database=app.config.get('DB_NAME'),
                user=app.config.get('DB_USER'),
                password=app.config.get('DB_PASSWORD'),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print("MariaDB에 성공적으로 연결되었습니다. (환경 변수 적용 완료)")
        except Error as e:
            print(f"MariaDB 연결 중 오류 발생: {e}")

    def save_bmi_record(self, weight, height, bmi, category):
        """BMI 기록을 데이터베이스에 저장"""
        try:
            if self.connection is None:
                print("데이터베이스 연결이 없습니다.")
                return False
                
            with self.connection.cursor() as cursor:
                query = """
                INSERT INTO bmi_records (weight, height, bmi, category)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (weight, height, bmi, category))
            
            self.connection.commit()
            return True
        except Error as e:
            print(f"데이터 저장 중 오류 발생: {e}")
            return False

    def get_bmi_records(self, limit=10):
        """최근 BMI 기록을 가져옵니다"""
        try:
            if self.connection is None:
                print("데이터베이스 연결이 없습니다.")
                return []
                
            with self.connection.cursor() as cursor:
                query = """
                SELECT * FROM bmi_records
                ORDER BY created_at DESC
                LIMIT %s
                """
                cursor.execute(query, (limit,))
                return cursor.fetchall()
        except Error as e:
            print(f"데이터 조회 중 오류 발생: {e}")
            return []

    def close(self):
        """데이터베이스 연결 종료"""
        if self.connection:
            self.connection.close()
            print("MariaDB 연결이 종료되었습니다.")

# 전역 DB 인스턴스 생성 (다른 모듈에서 import하여 사용)
db = Database()