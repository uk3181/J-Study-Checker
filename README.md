# 학습 및 성적 관리 시스템
학습 시간과 집중도를 분석하고 성적 변화 및 예측을 시각적으로 나타내어 사용자가 자신의 학습 습관과 성적 간의 상관관계를 파악할 수 있도록 돕는 애플리케이션이다.

## 프로젝트 개요
본 시스템은 일반 사용자(학생)를 대상으로 다양한 학습 도구를 하나의 애플리케이션에서 이용할 수 있도록 설계되었다.

### 주요 특징
- **학습 시간 기록**: 과목별 학습 시간을 기록하고 저장한다.
- **학습 시간 분석**: 날짜별·과목별로 학습 시간, 휴식 시간, 집중도를 분석한다.
- **성적 분석**: 입력된 항목별 성적을 분석하고 선형 회귀 분석을 통해 성적을 예측한다.
- **리마인더**: 지정된 날짜에 메모를 입력하고 해당 날짜가 되면 사용자에게 리마인더 알림으로 알려준다.

## 시스템 요구사항

### 운영 체제
- Windows

### 개발 환경
- **언어**: Python
- **플랫폼**: 데스크탑 애플리케이션

### 라이브러리
| 라이브러리 | 유형 | 용도 |
|-----------|------|------|
| tkinter | 내장 | GUI 프레임워크 (버튼, 레이블, 엔트리 등) |
| sortedcontainers | 외장 | 
| pickle | 내장 | 데이터 저장 및 관리 |
| datetime | 내장 | 날짜 및 시간 처리 |
| matplotlib | 외부 | 학습·성적 데이터 그래프 시각화 |

## 설치 및 실행

### 1. 애플리케이션 설치
- (1) 다운로드: [Installer 다운로드 링크](https://github.com/uk3181/J-Study-Checker/releases/download/v1.0/J.Study.Checker.Installer.exe)
- (2) 설치: J.Study.Checker.Installer.exe 실행 후 안내에 따라 설치 진행

### 2. 애플리케이션 실행
- Windows 시작 메뉴에서 앱 J Study Checker를 찾아서 실행

## 프로젝트 구조

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

## 사용자 유형별 기능

### 일반 사용자(학생)
- 기본적인 컴퓨터 사용 및 GUI 조작 능력을 갖추고 있다.
- 자신의 학습 과목 및 학습 계획을 관리할 수 있다.
- 학습 시간, 휴식 시간 및 성적 등의 정보를 직접 관리할 수 있다.
- 시스템에서 제공하는 학습 및 성적 분석 결과를 이해하고 활용할 수 있다.

## 주요 클래스

| 클래스 | 설명 |
|--------|------|
| `User` | 사용자의 기본 정보: ID, 비밀번호, 이름, 나이, 성별, 학습 데이터 목록, 성적 데이터 목록 등 |
| `StudyData` | 학습 데이터: 날짜, 과목명, 학습 시간 등 |
| `GradeData` | 성적 데이터: 날짜, 점수 등 |
| `ReminderData` | 리마인더 데이터: 날짜, 메모 |

## 개발자

| 이름 | GitHub |
|------|--------|
| 정재욱 | [@uk3181](https://github.com/uk3181) |

## 📝 라이선스

이 프로젝트는 교육 목적으로 개발되었습니다.
