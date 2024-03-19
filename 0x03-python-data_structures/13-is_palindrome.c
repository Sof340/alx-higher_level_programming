#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 * Return: 0 if false, 1 if true.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	freopen("/dev/null", "w", stdout);

	int size = print_listint(*head);

	freopen("/dev/tty", "w", stdout);

	if (size == 0)
		return (1);
	int array[size];

	int i;

	listint_t *current;

	current = *head;

	i = 0;

	while (current->next != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	array[size - 1] = current->n;

	for (; i < size / 2; i++)
	{
		if (array[i] != array[size - i - 1])
			return (0);
	}
	return (1);
}

