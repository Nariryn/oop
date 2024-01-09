def add_score(subject_score, student, subject, score):
  if student in subject_score:
      subject_score[student].update({subject: score})
  else:
      subject_score[student] = {subject: score}
  return subject_score

def calc_average_score(subject_score):
  student_average = {}
  for student, scores in subject_score.items():
      average_score = sum(scores.values()) / len(scores)
      student_average[student] = f"{average_score:.2f}"
  return student_average

subject_score = {}

while True:
    input_str = input("Enter student ID, subject, and score (or 'done' to finish): ")
    if input_str.lower() == 'done':
        break
    student, subject, score = map(str.strip, input_str.split(','))
    score = float(score)
    subject_score = add_score(subject_score, student, subject, score)

print("Subject_score: ", subject_score)
average_result = calc_average_score(subject_score)
print("Studen average: ",student, average_result)