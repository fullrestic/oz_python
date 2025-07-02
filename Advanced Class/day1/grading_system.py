def get_grade(score):
    """점수에 따른 등급 변환"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def analyze_and_display(students):
    """성적 분석 및 결과 출력"""
    scores = list(map(lambda s: s['score'], students))
    stats = {
        'average': sum(scores) / len(scores),
        'max_score': max(scores),
        'min_score': min(scores),
        'total_students': len(students)
    }

    # 등급 별 학생 수 계산 (filter 활용)
    grade_counts = {}
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = len(list(filter(lambda s: get_grade(s['score']) == grade, students)))
        grade_counts[grade] = count

    print("\n" + "="*50)
    print("성적 분석 결과")
    print("="*50)

    print(f"총 학생 수: {stats['total_students']}명")
    print(f"평균 점수 : {stats['average']:.1f}점")
    print(f"최고 점수 : {stats['max_score']}점")
    print(f"최저 점수 : {stats['min_score']}점")

    print("\n등급별 분포")
    for grade, count in grade_counts.items():
        print(f"{grade}등급: {count}명")

    print("\n학생 별 상세 성적:")
    sorted_students = sorted(students, key=lambda s: s['score'], reverse=True)
    for i, student in enumerate(sorted_students, 1):
        grade = get_grade(student['score'])
        print(f"{i:2d}. {student['name']:8s} {student['score']:3d}점 ({grade}등급)")

def main():
    students = []

    print("=== 성적 처리 프로그램 ===")
    while True:
        name = input("학생 이름 (종료: q) : ")
        if name.lower() == 'q':
            break

        try:
            score = int(input("점수: "))
            if 0 <= score <= 100:
                students.append({'name': name, 'score': score})
            else:
                print("점수는 0~100 사이여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    if not students:
        print("입력된 학생이 없습니다.")
        return

    analyze_and_display(students)

if __name__ == "__main__":
    main()