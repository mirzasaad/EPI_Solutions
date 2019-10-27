def finding_salaray_cap(target_payroll, current_salaries):
  current_salaries.sort()
  unadjusted_salaray_sum = 0.0
  for i, current_salary in enumerate(current_salaries):
    adjusted_people = len(current_salaries) - i
    adjusted_salary_sum = adjusted_people * current_salary
    if adjusted_salary_sum + unadjusted_salaray_sum >= target_payroll:
      return (target_payroll - unadjusted_salaray_sum) / adjusted_people
    unadjusted_salaray_sum += current_salary
  return -1.0

current_salaries = [20, 30, 40, 90, 100]
target_payroll = 210
print(finding_salaray_cap(target_payroll, current_salaries))