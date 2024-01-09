def add_score(subject_score, subject, score):
  subject_score.update({subject: score})
  return subject_score

def calc_average_score(subject_score):
  average_score = sum(subject_score.values())/len(subject_score)
  return '{:.2f}'.format(average_score)

subject_score = {}

max_subject = 2

while len(subject_score) < max_subject:
    subject = input("Enter subject: ")
    score = int(input ("Enter score: "))
    subject_score[subject] = score
#    subject_score = add_score(subject_score, subject, int(score))
print("Subject_score: ", subject_score)
print(calc_average_score(subject_score))
add_score()