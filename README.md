# 학습 및 성적 관리 시스템

<table id="table-of-contents">
  <tr>
    <td>
      <b>목차</b>
      <ul>
        <li><a href="#1-프로젝트-소개">1</a>. 프로젝트 소개</li>
        <li>
          <a href="#2-프로젝트-개요">2</a>. 프로젝트 개요
          <ul>
            <li><a href="#21-기존-시스템의-한계">2.1</a>. 기존 시스템의 한계</li>
            <li><a href="#22-기존-시스템의-한계를-보완한-새로운-시스템">2.2</a>. 기존 시스템의 한계를 보완한 새로운 시스템</li>
            <li><a href="#23-기존-시스템과-새로운-시스템의-기능-비교">2.3</a>. 기존 시스템과 새로운 시스템의 기능 비교</li>
          </ul>
        </li>
        <li>
          <a href="#3-사용자-유형-및-주요-기능">3</a>. 사용자 유형 및 주요 기능
          <ul>
            <li><a href="#31-일반-사용자학생">3.1</a>. 일반 사용자(학생)</li>
          </ul>
        </li>
        <li><a href="#4-시스템-범위">4</a>. 시스템 범위</li>
        <li><a href="#5-개발-환경-및-기술-스택">5</a>. 개발 환경 및 기술 스택</li>
        <li>
          <a href="#6-시스템-분석-및-설계">6</a>. 시스템 분석 및 설계
          <ul>
            <li>
              <a href="#61-시퀀스-다이어그램">6.1</a>. 시퀀스 다이어그램
              <ul>
                <li><a href="#611-사용자-관리-시스템-시퀀스-다이어그램">6.1.1</a>. 사용자 관리 시스템 시퀀스 다이어그램</li>
                <li><a href="#612-학습-시스템-시퀀스-다이어그램">6.1.2</a>. 학습 시스템 시퀀스 다이어그램</li>
                <li><a href="#613-학습-데이터-분석-시스템-시퀀스-다이어그램">6.1.3</a>. 학습 데이터 분석 시스템 시퀀스 다이어그램</li>
                <li><a href="#614-리마인더-시스템-시퀀스-다이어그램">6.1.4</a>. 리마인더 시스템 시퀀스 다이어그램</li>
                <li><a href="#615-학습-도구-시스템-시퀀스-다이어그램">6.1.5</a>. 학습 도구 시스템 시퀀스 다이어그램</li>
                <li><a href="#616-알림-시스템-시퀀스-다이어그램">6.1.6</a>. 알림 시스템 시퀀스 다이어그램</li>
              </ul>
            </li>
            <li>
              <a href="#62-활동-다이어그램">6.2</a>. 활동 다이어그램
              <ul>
                <li><a href="#621-사용자-관리-시스템-활동-다이어그램">6.2.1</a>. 사용자 관리 시스템 활동 다이어그램</li>
                <li><a href="#622-학습-시스템-활동-다이어그램">6.2.2</a>. 학습 시스템 활동 다이어그램</li>
                <li><a href="#623-학습-데이터-분석-시스템-활동-다이어그램">6.2.3</a>. 학습 데이터 분석 시스템 활동 다이어그램</li>
                <li><a href="#624-리마인더-시스템-활동-다이어그램">6.2.4</a>. 리마인더 시스템 활동 다이어그램</li>
                <li><a href="#625-학습-도구-시스템-활동-다이어그램">6.2.5</a>. 학습 도구 시스템 활동 다이어그램</li>
                <li><a href="#626-알림-시스템-활동-다이어그램">6.2.6</a>. 알림 시스템 활동 다이어그램</li>
              </ul>
            </li>
            <li>
              <a href="#63-클래스-다이어그램">6.3</a>. 클래스 다이어그램
              <ul>
                <li><a href="#631-사용자-관리-시스템-클래스-다이어그램">6.3.1</a>. 사용자 관리 시스템 클래스 다이어그램</li>
                <li><a href="#632-학습-시스템-클래스-다이어그램">6.3.2</a>. 학습 시스템 클래스 다이어그램</li>
                <li><a href="#633-학습-데이터-분석-시스템-클래스-다이어그램">6.3.3</a>. 학습 데이터 분석 시스템 클래스 다이어그램</li>
                <li><a href="#634-리마인더-시스템-클래스-다이어그램">6.3.4</a>. 리마인더 시스템 클래스 다이어그램</li>
                <li><a href="#635-학습-도구-시스템-클래스-다이어그램">6.3.5</a>. 학습 도구 시스템 클래스 다이어그램</li>
                <li><a href="#636-알림-시스템-클래스-다이어그램">6.3.6</a>. 알림 시스템 클래스 다이어그램</li>
              </ul>
            </li>
          </ul>
        </li>
        <li><a href="#7-배포-환경">7</a>. 배포 환경</li>
        <li><a href="#8-프로젝트-구조">8</a>. 프로젝트 구조</li>
        <li><a href="#9-개발팀">9</a>. 개발팀</li>
        <li><a href="#10-크레딧">10</a>. 크레딧</li>
        <li><a href="#11-라이선스">11</a>. 라이선스</li>
      </ul>
    </td>
  </tr>
</table>

## [1](#table-of-contents). 프로젝트 소개
J Study Checker는 학습 시간과 성적을 통합적으로 관리하고 분석할 수 있는 Windows 기반 학습 관리 프로그램이다. 학습 기록, 과목별 통계, 성적 분석 및 예측, 타이머 등의 기능을 제공한다.
- **프로젝트명:** 학습 및 성적 관리 시스템
- **프로젝트 유형:** 데스크탑 기반 학습 관리 애플리케이션
- **개발 목적:** 학생들이 단순히 학습만 하다 보면 체계적으로 관리가 안 될 때가 많다. 예를 들면, 학습 시간만 기록하고 순공부 시간은 기록하지 못해 집중도를 파악하지 못하는 경우가 있다. 또한 학습 시간과 휴식 시간을 분리하여 관리하지만 성적 변화 추이를 제대로 파악하지 못하는 경우도 있다. 본 시스템은 학습 시간과 휴식 시간을 분리해 관리하고 집중도를 분석하며, 성적 변화 및 예측을 시각적으로 나타내어 사용자가 자신의 학습 습관과 성적 간의 상관관계를 파악할 수 있도록 하였다. 이를 통해 성적이 상대적으로 부족한 과목을 보완할 수 있는 기대 효과를 가져온다.

## [2](#table-of-contents). 프로젝트 개요
### [2.1](#table-of-contents). 기존 시스템의 한계
열품타(YPT)는 사용자가 과목별 학습 시간을 측정하고 관리할 수 있도록 지원하는 학습 관리 애플리케이션이다. 또한 백색소음, 탁상모드, 학습 통계 등 학습을 지원하기 위한 다양한 기능을 제공한다. 그러나 기존의 학습 시간 관리 방식은 사용자의 실제 학습 활동과 학업 성취도를 함께 관리하고 분석하는 데 한계가 있다. 예를 들어 사용자가 오후 6시부터 오후 9시까지 수학을 학습하면서 오후 7시부터 7시 30분까지 휴식을 취한 경우, 실제 학습 시간은 2시간 30분이지만 전체 학습 세션에서 휴식이 차지하는 시간과 비율을 별도로 확인하기 어려울 수 있다. 또한 학습 시간 데이터와 성적 데이터를 통합적으로 관리하지 않는 경우, 사용자는 특정 과목에 투자한 학습 시간이 실제 성적 변화와 어떠한 관계가 있는지 체계적으로 확인하기 어렵다. 따라서 본 시스템은 학습 시간뿐만 아니라 휴식 시간과 성적 데이터를 함께 관리하고 분석하는 것을 목표로 한다.
### [2.2](#table-of-contents). 기존 시스템의 한계를 보완한 새로운 시스템
본 시스템은 학습 시간, 휴식 시간, 성적 데이터를 하나의 애플리케이션에서 통합적으로 관리하고 분석할 수 있도록 설계되었다. 사용자는 학습 중 학습 시작 및 종료 시간을 기록하고, 학습 도중 발생한 휴식 시간도 별도로 기록할 수 있다. 시스템은 이러한 데이터를 바탕으로 과목별 학습 시간과 휴식 시간 및 집중도를 분석한다. 사용자는 로그인 후 해당 날짜에 등록된 리마인더를 확인할 수 있으며, 학습 중에는 학습 및 휴식 시간을 기록할 수 있다. 학습을 종료한 후에는 축적된 학습 데이터와 성적 데이터를 기반으로 학습 및 성적 분석 기능을 이용할 수 있다. 본 시스템은 인터넷 연결 없이 독립적으로 실행할 수 있으며, 사용자 정보 및 학습·성적 데이터는 애플리케이션이 설치된 컴퓨터에 저장된다. 여러 사용자가 하나의 시스템에 등록할 수 있으며, 각 사용자는 GUI를 통해 자신의 과목, 학습 기록, 성적 및 리마인더 정보를 관리할 수 있다. 궁극적으로 본 시스템은 학습 시간뿐만 아니라 휴식 시간과 학업 성취도를 함께 관리함으로써, 기존의 단순 학습 시간 관리 방식에서 나아가 사용자가 자신의 학습 습관과 성적 변화를 종합적으로 확인할 수 있도록 지원한다.
### [2.3](#table-of-contents). 기존 시스템과 새로운 시스템의 기능 비교
|   | 열품타 | J Study Checker |
| - | :--: | :--------------: |
| **학습 시간 측정** | 지원 | 지원 |
| **과목별 학습 시간 관리** | 지원 | 지원 |
| **학습 시간 통계** | 지원 | 지원 |
| **휴식 시간 측정** | 미지원 | 지원 |
| **집중도 분석** | 미지원 | 지원 |
| **과목별 성적 관리** | 미지원 | 지원 |
| **학습 시간과 성적의 관계 분석** | 미지원 | 지원 |
| **성적 예측** | 미지원 | 지원 |

## [3](#table-of-contents). 사용자 유형 및 주요 기능
### [3.1](#table-of-contents). 일반 사용자(학생)
- 기본적인 컴퓨터 사용 및 GUI 조작 능력을 갖추고 있다.
- 자신의 학습 과목 및 학습 계획을 관리할 수 있다.
- 학습 시간, 휴식 시간 및 성적 등의 정보를 직접 관리할 수 있다.
- 시스템에서 제공하는 학습 및 성적 분석 결과를 이해하고 활용할 수 있다.

## [4](#table-of-contents). 시스템 범위
| 시스템 | 설명 |
| ------- | --- |
| **학습 시간 기록** | 과목별 학습 시간을 기록하고 저장한다. |
| **학습 시간 분석** | 날짜별·과목별로 학습 시간, 휴식 시간, 집중도를 분석한다. |
| **성적 분석** | 입력된 성적 데이터를 과목 및 날짜별로 분석하고, 선형 회귀 모델을 이용하여 향후 성적을 예측한다. |
| **리마인더** | 지정된 날짜에 메모를 입력하고 해당 날짜가 되면 사용자에게 리마인더 알림으로 알려준다. |

## [5](#table-of-contents). 개발 환경 및 기술 스택
- **Language:** Python
- **GUI:** Tkinter
- **Data Analysis:** Numpy, Scikit-learn
- **Visualization:** Matplotlib
- **Data Management:** Pickle, SortedContainters, Datetime
- **Libraries**
  - tkinter: GUI 프레임워크 (버튼, 레이블, 엔트리 등)
  - sortedcontainers: 정렬된 상태의 데이터 관리
  - datetime: 날짜 및 시간 처리
  - matplotlib: 학습·성적 데이터 그래프 시각화
  - math: 수학 계산 처리
  - numpy: 숫자·배열의 빠른 계산 처리
  - sklearn.linear_model: 선형 회귀 모델을 이용한 성적 예측
  - pathlib: 파일과 폴더의 경로 관리
  - pickle: Python 객체의 직렬화 및 역직렬화

## [6](#table-of-contents). 시스템 분석 및 설계
### [6.1](#table-of-contents). 시퀀스 다이어그램
#### [6.1.1](#table-of-contents). 사용자 관리 시스템 시퀀스 다이어그램
- 사용자 등록<br>
  ![](./docs/images/diagrams/sequence_diagram_1_1.jpg)<br>
- 로그인<br>
  ![](./docs/images/diagrams/sequence_diagram_1_2.jpg)
#### [6.1.2](#table-of-contents). 학습 시스템 시퀀스 다이어그램
- 학습<br>
  ![](./docs/images/diagrams/sequence_diagram_2_1.jpg)
#### [6.1.3](#table-of-contents). 학습 데이터 분석 시스템 시퀀스 다이어그램
- 학습 분석<br>
  ![](./docs/images/diagrams/sequence_diagram_3_1.jpg)<br>
- 성적 분석<br>
  ![](./docs/images/diagrams/sequence_diagram_3_2.jpg)
#### [6.1.4](#table-of-contents). 리마인더 시스템 시퀀스 다이어그램
- 리마인더 관리<br>
  ![](./docs/images/diagrams/sequence_diagram_4_1.jpg)
#### [6.1.5](#table-of-contents). 학습 도구 시스템 시퀀스 다이어그램
생략
#### [6.1.6](#table-of-contents). 알림 시스템 시퀀스 다이어그램
- 리마인더 알림 업데이트<br>
  ![](./docs/images/diagrams/sequence_diagram_6_1.jpg)<br>
- 사용자 정보 변경 알림 업데이트<br>
  ![](./docs/images/diagrams/sequence_diagram_6_2.jpg)
### [6.2](#table-of-contents). 활동 다이어그램
#### [6.2.1](#table-of-contents). 사용자 관리 시스템 활동 다이어그램
- 사용자 등록<br>
  ![](./docs/images/diagrams/activity_diagram_1_1.jpg)<br>
- 로그인<br>
  ![](./docs/images/diagrams/activity_diagram_1_2.jpg)
#### [6.2.2](#table-of-contents). 학습 시스템 활동 다이어그램
- 학습 시작<br>
  ![](./docs/images/diagrams/activity_diagram_2_1.jpg)<br>
- 학습 기록 저장<br>
  ![](./docs/images/diagrams/activity_diagram_2_2.jpg)
#### [6.2.3](#table-of-contents). 학습 데이터 분석 시스템 활동 다이어그램
- 학습 분석<br>
  ![](./docs/images/diagrams/activity_diagram_3_1.jpg)<br>
- 성적 데이터 입력<br>
  ![](./docs/images/diagrams/activity_diagram_3_2.jpg)<br>
- 성적 데이터 분석<br>
  ![](./docs/images/diagrams/activity_diagram_3_3.jpg)
#### [6.2.4](#table-of-contents). 리마인더 시스템 활동 다이어그램
- 리마인더 수정<br>
  ![](./docs/images/diagrams/activity_diagram_4_1.jpg)
#### [6.2.5](#table-of-contents). 학습 도구 시스템 활동 다이어그램
생략
#### [6.2.6](#table-of-contents). 알림 시스템 활동 다이어그램
- 리마인더 알림 업데이트<br>
  ![](./docs/images/diagrams/activity_diagram_6_1.jpg)<br>
- 사용자 정보 변경 알림 업데이트<br>
  ![](./docs/images/diagrams/activity_diagram_6_2.jpg)
### [6.3](#table-of-contents). 클래스 다이어그램
#### [6.3.1](#table-of-contents). 사용자 관리 시스템 클래스 다이어그램
![](./docs/images/diagrams/class_diagram_1.jpg)
#### [6.3.2](#table-of-contents). 학습 시스템 클래스 다이어그램
![](./docs/images/diagrams/class_diagram_2.jpg)
#### [6.3.3](#table-of-contents). 학습 데이터 분석 시스템 클래스 다이어그램
![](./docs/images/diagrams/class_diagram_3.jpg)
#### [6.3.4](#table-of-contents). 리마인더 시스템 클래스 다이어그램
![](./docs/images/diagrams/class_diagram_4.jpg)
#### [6.3.5](#table-of-contents). 학습 도구 시스템 클래스 다이어그램
![](./docs/images/diagrams/class_diagram_5.jpg)
#### [6.3.6](#table-of-contents). 알림 시스템 클래스 다이어그램
![](./docs/images/diagrams/class_diagram_6.jpg)

## [7](#table-of-contents). 배포 환경
- **다운로드:** https://github.com/uk3181/J-Study-Checker/releases/download/v1.0/J.Study.Checker.Installer.exe
- **설치:** J.Study.Checker.Installer.exe 실행 후 안내에 따라 설치 진행

## [8](#table-of-contents). 프로젝트 구조
<details>
<summary>프로젝트 구조</summary>

```
J-Study-Checker/
├── .github/
│   └── workflows/
│       └── build.yml
├── Datas/ # 사용자 및 학습 데이터 저장
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
│   ├── Graphs/ # 학습 및 성적 데이터를 시각화한 그래프
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
├── SourceCodes/ # 프로그램의 주요 GUI 및 기능 구현
│   ├── analysis_grades_frame.py # 성적 분석 프레임
│   ├── analysis_grades.py # 성적 분석 시스템 - 성적 예측, 성적 분석 그래프 생성 등
│   ├── analysis_study.py # 학습 분석 시스템 - 학습 분석 그래프 생성 등
│   ├── analysis_study_frame.py # 학습 분석 프레임
│   ├── app.py # 최종적으로 실행되는 앱
│   ├── calculator_frame.py # 계산기 프레임
│   ├── home_frame.py # 홈 프레임 - 시스템의 다양한 기능을 선택하여 실행시킬 수 있음.
│   ├── login_frame.py # 로그인 프레임 - 앱을 실행하였을 때 나타남.
│   ├── menu_button.py # 메뉴 버튼 UI 구현
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

</details>

## [9](#table-of-contents). 개발팀
| 이름 | GitHub | 담당 역할 |
| --- | ------ | ------- |
| 정재욱 | [@uk3181](https://github.com/uk3181) | Python 개발 |
| AI Agent | - | 소스 파일 analysis_grades.py 작성 보조 |

## [10](#table-of-contents). 크레딧
| 역할 | 이름 |
| --- | --- |
| Program Planning | 정재욱 |
| System Design | 정재욱 |
| Programming | 정재욱 |
| GUI Design | 정재욱, Pixabay |
| Data Analysis | 정재욱, AI Agent |

## [11](#table-of-contents). 라이선스
Copyright © 2026 J Study Checker. All rights reserved.<br>
본 프로젝트의 소스 코드는 교육 목적으로 작성되었으며, 저작권자의 사전 허가 없이 복제, 수정, 배포 및 상업적 이용을 할 수 없다.
