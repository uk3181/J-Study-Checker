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
| sortedcontainers | 외장 | 정렬된 상태의 데이터 관리 |
| datetime | 내장 | 날짜 및 시간 처리 |
| matplotlib | 외부 | 학습·성적 데이터 그래프 시각화 |
| math | 내부 | 수학 계산 처리 |
| numpy | 외부 | 숫자·배열의 빠른 계산 처리 |
| sklearn.linear_model | 외부 | 선형 모델을 이용한 성적 예측 |
| path lib | 내부 | 파일과 폴더의 경로 관리 |
| pickle | 내장 | 데이터 저장 및 관리 |

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
│   └── user_list.bin # 시스템의 데이터를 이진 파일로 관리함.
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
│   ├── Backgrounds/ # 각 프레임의 배경화면
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
│   ├── Graphs/ # 학습 관련 데이터를 시각화한 그래프
│   │   ├── break_time_per_days_graph.png
│   │   ├── break_time_per_subjects_graph.png
│   │   ├── focus_rate_per_days_graph.png
│   │   ├── focus_rate_per_subjects_graph.png
│   │   ├── grade_data_graph.png
│   │   ├── studying_time_per_days_graph.png
│   │   └── studying_time_per_subjects_graph.png
│   └── Icons/ # 애플리케이션 및 각 버튼의 아이콘
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
│   ├── analysis_grades_frame.py # 성적 분석 프레임
│   ├── analysis_study.py # 학습 분석 시스템 - 학습 분석 그래프 생성 등
│   ├── analysis_study_frame.py # 학습 분석 프레임
│   ├── anaylsis_grades.py # 성적 분석 시스템 - 성적 예측, 성적 분석 그래프 생성 등
│   ├── app.py # 최종적으로 실행되는 앱
│   ├── calculator_frame.py # 계산기 프레임
│   ├── home_frame.py # 홈 프레임 - 시스템의 다양한 기능을 선택하여 실행시킬 수 있음.
│   ├── login_frame.py # 로그인 프레임 - 앱을 실행하였을 때 나타남.
│   ├── menu_button.py
│   ├── notification_frame.py # 알림 프레임
│   ├── notification_system.py # 알림 시스템 - 리마인더 알림 업데이트, 사용자 정보 변경 알림 업데이트
│   ├── path_settings.py # 모든 소스코드의 기본 경로를 설정함.
│   ├── register_frame.py # 회원가입 프레임
│   ├── reminder_frame.py # 리마인더 프레임
│   ├── reset_file.py # 시스템의 데이터를 초기화하는 코드
│   ├── stopwatch_frame.py # 스톱워치 프레임
│   ├── study_frame.py # 학습 프레임
│   ├── time_table_frame.py # 요일별 학습 시간을 보여주는 프레임
│   ├── timer_frame.py # 타이머 프레임
│   ├── user.py # 사용자 클래스 및 시스템 - 사용자 추가, 수정, 삭제
│   └── user_frame.py # 사용자 프레임
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

## 라이선스
Copyright © 2026 J Study Checker. All rights reserved.<br>
본 프로젝트의 소스 코드는 교육 목적으로 작성되었으며, 저작권자의 사전 허가 없이 복제, 수정, 배포 및 상업적 이용을 할 수 없다.
