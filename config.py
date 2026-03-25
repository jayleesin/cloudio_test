import os
from dotenv import load_dotenv

# .env 파일의 환경 변수를 시스템 환경 변수로 로드
load_dotenv()

class Config:
    """기본 공통 설정"""
    # Flask 기본 보안 설정 (세션 등에 사용)
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-for-dev')
    
    # DB 연결 설정 (.env에서 값을 가져오고, 없으면 기본값 사용)
    DB_HOST = os.getenv('DB_HOST', 'mariadb')
    DB_PORT = int(os.getenv('DB_PORT', 3306))
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'master')
    DB_NAME = os.getenv('DB_NAME', 'test')

class DevelopmentConfig(Config):
    """개발 환경 설정"""
    DEBUG = True
    # 개발 환경 특화 설정이 필요하다면 여기에 추가

class ProductionConfig(Config):
    """운영 환경 설정"""
    DEBUG = False
    # 운영 환경 특화 설정이 필요하다면 여기에 추가

# 환경에 따라 설정을 쉽게 불러오기 위한 딕셔너리
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}