#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

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

