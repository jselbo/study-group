#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char sum_and_ret_values(int *rem, char dig0, char dig1)
{
	int x = (int) dig0 - 48;
	int y = (int) dig1 - 48;
	int sum = *rem + x + y;
	*rem = sum / 10;
	sum = sum % 10;

	return (char) (sum + 48);
}

int main(int argc, char **argv)
{
	int ret, i, j, rem = 0;
	unsigned long long num1_len, num2_len;
	unsigned long long res_len, count_len;

	if (argc != 3) {
		printf("Please provide exactly 2 arguments\n");
		return -1;
	}

	num1_len = strlen(argv[1]);
	num2_len = strlen(argv[2]);
	count_len = res_len = num1_len < num2_len ? num2_len + 1 : num1_len + 1;

	char res_num[res_len+1];
	res_num[res_len] = '\0';

	for (i = num1_len - 1, j = num2_len - 1; i >= 0 && j >= 0; i--, j--)
		res_num[--res_len] = sum_and_ret_values(&rem, argv[1][i], argv[2][j]);

	while (i >= 0)
		res_num[--res_len] = sum_and_ret_values(&rem, argv[1][i--], '0');

	while (j >= 0)
		res_num[--res_len] = sum_and_ret_values(&rem, '0', argv[2][j--]);

	for (i = 0; i < count_len; i++)
		printf("%c", res_num[i]);
	printf("\n");

	return 0;
};
