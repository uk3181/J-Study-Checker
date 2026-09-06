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
├── .github/
│   └── workflows/
│       └── build.yml
├── Datas/
│   └── user_list.bin
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
│   │   ├── analysis_grades_background.png
│   │   ├── analysis_study_background.png
│   │   ├── calculator_background.png
│   │   ├── home_background.png
│   │   ├── login_background.png
│   │   ├── notification_background.png
│   │   ├── register_background.png
│   │   ├── reminder_background.png
│   │   ├── stopwatch_background.png
│   │   ├── study_background.png
│   │   ├── study_calendar_background.png
│   │   ├── time_table_background.png
│   │   ├── timer_background.png
│   │   └── user_background.png
│   ├── Graphs/
│   │   ├── break_time_per_days_graph.png
│   │   ├── break_time_per_subjects_graph.png
│   │   ├── focus_rate_per_days_graph.png
│   │   ├── focus_rate_per_subjects_graph.png
│   │   ├── grade_data_graph.png
│   │   ├── studying_time_per_days_graph.png
│   │   └── studying_time_per_subjects_graph.png
│   └── Icons/
│   │   ├── app_icon.png
│   │   ├── custom_timer_button_1.png
│   │   ├── custom_timer_button_2.png
│   │   ├── five_minutes_timer_button_1.png
│   │   ├── five_minutes_timer_button_2.png
│   │   ├── notification_icon_1.png
│   │   ├── notification_icon_2.png
│   │   ├── one_minute_timer_button_1.png
│   │   ├── one_minute_timer_button_2.png
│   │   ├── ten_minutes_timer_button_1.png
│   │   ├── ten_minutes_timer_button_2.png
│   │   ├── user_icon_1.png
│   │   └── user_icon_2.png
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
├── README.md
├── System Modeling and Design.pdf
├── System Requirements Specification.pdf
└── privacy-policy.html
```

## 👥 사용자 유형별 기능

### 🏥 일반 사용자(학생)
- 기본적인 컴퓨터 사용 및 GUI 조작 능력을 갖추고 있다.
- 자신의 학습 과목 및 학습 계획을 관리할 수 있다.
- 학습 시간, 휴식 시간 및 성적 등의 정보를 직접 관리할 수 있다.
- 시스템에서 제공하는 학습 및 성적 분석 결과를 이해하고 활용할 수 있다.

## 🔧 주요 클래스

| 클래스 | 설명 |
|--------|------|
| `Data` | 날짜별 건강 수치 저장 (혈압, 혈당, BMI, 영양소, 운동량 등) |
| `User` | 모든 사용자의 기본 정보 (이름, 나이, ID, PW, 알림 등) |
| `Patient` | 개인 사용자 - 건강 데이터, 친구 목록, 인센티브 점수 관리 |
| `Doctor` | 주치의 - 담당 환자 목록, 초대 코드 관리 |
| `Parent` | 보호자 - 연결된 환자 목록 관리 |

## 👨‍💻 개발자

| 이름 | GitHub |
|------|--------|
| 정재욱 | [@uk3181](https://github.com/uk3181) |

## 📝 라이선스

이 프로젝트는 교육 목적으로 개발되었습니다.
