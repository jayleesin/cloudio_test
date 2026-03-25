from flask import Flask
import atexit

# 1~4단계에서 분리한 모듈들을 Import 합니다.
from config import config
from backend.models.db import db
from backend.routes.main_routes import main_bp

def create_app(config_name='default'):
    """
    App Factory 함수: Flask 애플리케이션 인스턴스를 생성하고 초기화합니다.
    """
    app = Flask(__name__)
    
    # 1. 환경 설정 적용 (config.py의 설정 클래스를 앱에 주입)
    app.config.from_object(config[config_name])
    
    # 2. 데이터베이스 초기화 (생성된 app 인스턴스와 DB를 연결)
    db.init_app(app)
    
    # 애플리케이션 종료 시 DB 연결을 안전하게 닫도록 등록
    atexit.register(db.close)
    
    # 3. Blueprint 등록 (분리해둔 URL 라우팅을 앱에 부착)
    app.register_blueprint(main_bp)
    
    return app

# 스크립트가 직접 실행될 때 구동되는 개발용 서버 설정
if __name__ == '__main__':
    # 개발(development) 모드로 앱 인스턴스 생성
    app = create_app('development')
    
    # 실행 (debug 모드 여부는 config.py에서 이미 제어 중입니다)
    app.run(host='0.0.0.0', port=5000)