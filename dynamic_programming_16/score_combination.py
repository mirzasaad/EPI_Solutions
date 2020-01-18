def num_combinations_for_final_score(final_score, individual_play_scores):
  # One way to reach 0.
  num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]

  for row in range(len(individual_play_scores)):
    for col in range(1, final_score + 1):
      without_this_play = num_combinations_for_score[row - 1][col] if row >= 1 else 0
      with_this_play = num_combinations_for_score[row][col - individual_play_scores[row]] if col >= individual_play_scores[row] else 0
      num_combinations_for_score[row][col] = without_this_play + with_this_play
  return num_combinations_for_score[-1][-1]

individual_play_scores = [2, 3, 7]
assert 4 == num_combinations_for_final_score(12, individual_play_scores)
assert 1 == num_combinations_for_final_score(5, individual_play_scores)
assert 3 == num_combinations_for_final_score(9, individual_play_scores)