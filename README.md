# 뇌졸중 위험도 산출 기반 건강 관리 시스템

뇌졸중 위험도 산출을 기반으로 한 경쟁 시스템을 통해 생활습관을 개선하고 뇌졸중 예방 활동을 돕는 데스크탑 애플리케이션입니다.

## 📋 프로젝트 개요

본 시스템은 세 가지 사용자 그룹(개인 사용자, 보호자, 의사)을 대상으로 각 그룹에 맞는 맞춤 서비스를 제공하여 그룹 간의 유기적인 상호작용을 촉진합니다.

### 주요 특징
- **건강 데이터 관리**: 혈압, 혈당, BMI, 식단, 운동량 등 일별 건강 데이터 기록 및 조회
- **위험도 산출**: 로지스틱 모델을 이용한 뇌졸중 위험도 분석
- **경쟁 시스템**: 친구 간 점수 비교 및 뱃지 수여를 통한 동기부여
- **알림 시스템**: 고위험 시 본인 및 보호자에게 자동 알림 발송
- **콘텐츠 관리**: 주치의가 환자별 건강 목표 및 권고사항 설정

## 🛠 시스템 요구사항

### 운영 체제
- Windows

### 개발 환경
- **언어**: Python
- **플랫폼**: 데스크탑 애플리케이션

### 라이브러리
| 라이브러리 | 유형 | 용도 |
|-----------|------|------|
| tkinter | 내장 | GUI 프레임워크 (버튼, 레이블, 입력창 등) |
| pickle | 내장 | 데이터 저장 및 관리 |
| datetime | 내장 | 날짜 및 시간 처리 |
| math | 내장 | 위험도 산출 모델 계산 |
| matplotlib | 외부 | 건강 데이터 그래프 시각화 |

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/molto-piu-tranquillo/swdesign.git
cd swdesign
```

### 2. 애플리케이션 실행
```bash
cd workspace/SourceCodes
python app.py
```

> **참고**: matplotlib가 설치되어 있지 않은 경우 실행 시 자동으로 설치됩니다.

## 📁 프로젝트 구조

```
J-Study-Checker/
├── Datas/
│   └── user_list.bin #
├── Fonts/
│   └── NanumGothic/
│       └── NanumGothic/
│           ├── NanumGothic.otf
│           ├── NanumGothic.ttf
│           ├── NanumGothicBold.otf
│           ├── NanumGothicBold.ttf
│           ├── NanumGothicExtraBold.otf
│           ├── NanumGothicExtraBold.ttf
│           ├── NanumGothicLight.otf
│           └── NanumGothicLight.ttf
├── Images/
│   ├── Backgrounds/
│   ├── Graphs/
│   └── Icons/
├── SourceCodes/
│   ├── analysis_grades_frame.py #
│   ├── analysis_study.py #
│   ├── analysis_study_frame.py #
│   ├── anaylsis_grades.py #
│   ├── app.py #
│   ├── calculator_frame.py #
│   ├── home_frame.py #
│   ├── login_frame.py #
│   ├── menu_button.py #
│   ├── notification_frame.py #
│   ├── notification_system.py #
│   ├── path_settings.py #
│   ├── register_frame.py #
│   ├── reminder_frame.py #
│   ├── reset_file.py #
│   ├── stopwatch_frame.py #
│   ├── study_frame.py #
│   ├── time_table_frame.py #
│   ├── timer_frame.py #
│   ├── user.py #
│   └── user_frame.py #
├── Datas/
│   └── userlist.bin
└── README.md
```

## 👥 사용자 유형별 기능

### 🏥 개인 사용자 (환자)
- **건강 데이터 관리**
  - 일별 건강 데이터 입력 (혈압, 혈당, 키, 체중, 흡연/음주 여부, 영양소 섭취량, 운동량)
  - 날짜별 데이터 조회
  - 건강 추이 그래프 확인
- **위험도 분석**
  - 최신 데이터 기반 위험도 산출
  - 항목별 경고 표시
  - 고위험 시 자동 알림 발송
- **개인 리포트**
  - 혈압, 혈당, 섭취량, 활동량 시계열 그래프
  - 목표 설정 및 저장
- **경쟁 시스템**
  - 친구 추가/삭제
  - 뱃지 수여 및 확인
  - 인센티브 점수 확인
- **연결 기능**
  - 보호자 연결 (초대 코드 생성)
  - 주치의 연결 (초대 코드 생성)
- **콘텐츠**
  - 주치의가 작성한 콘텐츠 확인
  - 콘텐츠 변경 요청

### 👨‍⚕️ 주치의
- **환자 관리**
  - 초대 코드를 통한 환자 등록
  - 환자 패널에서 환자 정보 조회 (기본정보, 위험도, 건강 추이, 목표)
  - 이전/다음 버튼으로 환자 카드 탐색
- **인센티브 부여**
  - 최근 2건의 데이터 비교 후 인센티브 점수 계산 및 반영
- **진료 관리**
  - 다음 진료일 설정
  - 환자에게 리마인더 전송
- **콘텐츠 관리**
  - 환자별 콘텐츠 (건강 목표, 권고사항) 작성
  - 환자의 변경 요청 확인 및 처리

### 👪 보호자
- **가족 연결**
  - 환자 ID와 초대 코드로 연결
- **모니터링**
  - 연결된 환자의 위험도 알림 수신
- **소통**
  - 메시지 기능을 통한 환자/의사와 의사소통

## 🔧 주요 클래스

| 클래스 | 설명 |
|--------|------|
| `Data` | 날짜별 건강 수치 저장 (혈압, 혈당, BMI, 영양소, 운동량 등) |
| `User` | 모든 사용자의 기본 정보 (이름, 나이, ID, PW, 알림 등) |
| `Patient` | 개인 사용자 - 건강 데이터, 친구 목록, 인센티브 점수 관리 |
| `Doctor` | 주치의 - 담당 환자 목록, 초대 코드 관리 |
| `Parent` | 보호자 - 연결된 환자 목록 관리 |

## 👨‍💻 개발팀 (Team 11)

| 이름 | GitHub | 담당 기능 |
|------|--------|----------|
| 김민수 | [@molto-piu-tranquillo](https://github.com/molto-piu-tranquillo) | 위험도 산출 프레임, 환자 관리 패널, 리마인더 기능 |
| 김민균 | [@Aurelia-aurity](https://github.com/Aurelia-aurity) | 메인프레임, 콘텐츠 추가/요청 기능, 코드 통합 |
| 조민지 | [@m0nzz1](https://github.com/m0nzz1) | 로그인프레임, 식단 추천 기능 |
| 정재욱 | [@uk3181](https://github.com/uk3181) | 가족/주치의 연결, 건강 데이터 분석, 알림/메시지, 친구 기능 |

## 📝 라이선스

이 프로젝트는 교육 목적으로 개발되었습니다.
