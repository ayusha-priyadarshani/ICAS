#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//#include "linked_list.h"
int main()
{
    do
    {
        printf(" Enter your choice:\n 1. Registrar login\t 2. Judge login\t 3. Lawyer login\t 4. Exit\n");
        int ch;
        scanf("%d", &ch);
        char resp;

        switch (ch)
        {
            case 1: registrar();
                break;
            case 2: //judge
                break;
            case 3: //lawyer
                break;
            case 4: exit(0);
            default: printf("\n Enter a valid choice!\n");
        }
    } while (resp == 'y' || resp == 'Y');
    return 0;
}
void registrar()
{
    int emp_no;
    printf("Enter employee number: ");
    scanf("%d", &emp_no);

    char pwd[15];
    print("Enter password: ");
    scanf("%s", pwd);

    printf("\n Enter your choice:\n 1. Query cases\t 2. Manage accounts\n");
    int ch;
    scanf("%d", &ch);

    switch (ch)
    {
        case 1: printf("\n Enter your choice:\n 1. Generate CIN\t 2. Schedule hearing\t 3. Record case summary\n 4. Browse cases\t 5. Check case status\n");
                int ch1;
                scanf("%d", &ch1);

                switch (ch1)
                {
                    case 1: insertLast();
                            int cin = 1034;
                            printf("Case CIN generated: %d", cin);
                            cin++;
                            break;

                    default: printf("\n Enter a valid choice!\n");
                }
                break;
        case 2: printf(" Enter you choice:\n 1. Create account\t 2. Delete account\t 3. View browsing activity\n");
                int ch2;
                scanf("%d", &ch2);

                switch (ch2)
                {
                    case 1: printf("\n Enter employee number: ");
                            int emp_no;
                            scanf("%d", emp_no);
                            printf(" Enter password: ");
                            char pwd[15];
                            scanf(" %s", pwd);

                            printf("\n Account created successfully!\n");
                            break;

                    case 2: printf("\n Enter employee number: ");
                            //int emp_no;
                            scanf("%d", &emp_no);
                            printf(" Enter password: ");
                            //char pwd[];
                            scanf("%s", pwd);

                            printf("\n Account has been deleted\n");
                            break;

                    case 3: printf(" Enter employee number: ");
                            //int emp_no;
                            scanf("%d", &emp_no);
                            //show case browsing history

                    default: printf("\n Enter a valid choice!\n");
                }
                break;
        default: printf("\n Enter a valid choice!\n");
    }
}

#include <stdio.h>
#include<stdlib.h>
//#include"func.c"
#include"linked list base.c"


void judge()
{
    int emp_id, password;
    printf("Enter ID:");
    scanf("%d", &emp_id);
    printf("Enter Password:");
    scanf("%d", &password);

    int choice;

    do
    {
        printf("\n1. Browse Files\n2. Logout\n\nChoose your option:  ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1: browse_old_files();
            case 2: exit(0);

            default: printf("\nEnter a valid option!");
        }
    }while (1);
}

void lawyer()
{
    int emp_id, password;
    printf("Enter ID:");
    scanf("%d", &emp_id);
    printf("Enter Password:");
    scanf("%d", &password);

    int choice;

    do
    {
        printf("\n1. Browse Files\n2. Logout\n\nChoose your option:  ");
        scanf("%d", &choice);

        char rand;
        switch(choice)
        {
            case 1: printf("\n\n\n\t**CLICK HERE TO PAY**\t\n\n\n");
                    scanf("%s", &rand);
                    printf("\nThank you\n\n");
                    browse_old_files();
            case 2: exit(0);

            default: printf("\nEnter a valid option!");
        }
    }while (1);
}

int main()
{
    //judge();
    lawyer();
}
#include <stdio.h>
#include <stdlib.h>
#include<string.h>

/*
what details do i need to print for ongoing cases
*/


int file_views=0;
int base_cin=2208000;

struct NODE
        {
            int CIN;
            int start_date;
            char defendants_name[20];
            char defendants_address[50];
            char crime[20];
            char lawyers_name[20];
            char prosecutors_name[20];
            char judges_name[20];
            char status[20];
            int close_date;
            struct NODE *next;
        };
typedef struct NODE node;
node *head= NULL;

void new_entry()
{
    node *temp= (node*) malloc (sizeof(node));
    if (temp==NULL)
    {
        printf("Memory allocation fails");
        return;
    }

    temp->CIN=base_cin;
    strcpy(temp->status,"ONGOING");
    temp->close_date=0000;
    base_cin++;

    int number;
    printf("\nSTART DATE:");
    scanf("%d", &number);
    temp->start_date=number;

    //char *sents;
    //char sents[50];
    printf("\nNAME OF DEFENDANT:");
    char defendants_name[20];
    scanf("%s", defendants_name);
    //gets(temp->defendants_name);
    strcpy(temp->defendants_name,defendants_name);
    //temp->defendants_name=sents;
    //printf("%s\n", temp->defendants_name);

    printf("\nADDRESS OF DEFENDANT:");
    char defendants_address[20];
    scanf("%s", defendants_address);
    //temp->defendants_address=sents;
    strcpy(temp->defendants_address,defendants_address);
    //printf("%s",temp->defendants_address);
    //temp->defendants_address=sents;

    printf("\nCRIME:");
    char crime[15];
    scanf("%s", crime);
    //temp->crime=sents;
    strcpy(temp->crime,crime);
    //temp->crime=crime;

    printf("\nNAME OF LAWYER:");
    char lawyers_name[20];
    scanf("%s", lawyers_name);
    //temp->lawyers_name=sents;
    strcpy(temp->lawyers_name,lawyers_name);
    //temp->lawyers_name=lawyers_name;

    printf("\nNAME OF PROSECUTOR:");
    char prosecutors_name[20];
    scanf("%s", prosecutors_name);
    //temp->prosecutors_name=sents;
    strcpy(temp->prosecutors_name,prosecutors_name);
    //temp->prosecutors_name=prosecutors_name;

    printf("\nNAME OF JUDGE: ");
    char judges_name[20];
    scanf("%s", judges_name);
    //temp->judges_name=sents;
    strcpy(temp->judges_name,judges_name);
    //temp->judges_name=judges_name;

    temp->next=NULL;
    if(head==NULL)
    {
        head= temp;
        return;
    }
    node *cur=head;
    while(cur->next!=NULL)
    {
        cur=cur->next;
    }
    cur->next=temp;
}

void create()
{
    char ans='y';
    do
    {
        printf("\n\n\n\n\tCIN: %d\t\n\n\n", base_cin);
        new_entry();

        printf("\nMake another entry? (y/n) ");
        scanf("%s", &ans);
    }while (ans=='y'||ans=='Y');
}

void search_by_cin()
{
    int cin;
    printf("\nEnter CIN: ");
    scanf("%d", &cin);

    node *cur=head;
    while(cur->CIN!=cin)
    {
        cur=cur->next;
    }

    printf("\n\n\n\n\tCIN: %d",cur->CIN);
    printf("\n\nSTART DATE: %d",cur->start_date);
    printf("\n\nNAME OF DEFENDANT: ");
    printf("%s",cur->defendants_name);
    printf("\n\nADDRESS OF DEFENDANT: %s",cur->defendants_address);
    printf("\n\nCRIME: %s",cur->crime);
    printf("\n\nNAME OF LAWYER: %s",cur->lawyers_name);
    printf("\n\nNAME OF PROSECUTOR: %s",cur->prosecutors_name);
    printf("\n\nNAME OF JUDGE: %s",cur->judges_name);
    printf("\n\nSTATUS: %s",cur->status);
    printf("\n\nCLOSE DATE: %d",cur->close_date);

    file_views++;
}


void search_by_keyword()
{
    char key[15];
    printf("\nEnter crime:");
    scanf("%s",key);

    node *cur=head;
    while(cur->next!=NULL)
    {
        if (strcmp(key,cur->crime)==0)
        {
            printf("\n\n\n\n\tCIN: %d",cur->CIN);
            printf("\n\nSTART DATE: %d",cur->start_date);
            printf("\n\nNAME OF DEFENDANT: ");
            printf("%s",cur->defendants_name);
            printf("\n\nADDRESS OF DEFENDANT: %s",cur->defendants_address);
            printf("\n\nCRIME: %s",cur->crime);
            printf("\n\nNAME OF LAWYER: %s",cur->lawyers_name);
            printf("\n\nNAME OF PROSECUTOR: %s",cur->prosecutors_name);
            printf("\n\nNAME OF JUDGE: %s",cur->judges_name);
            printf("\n\nSTATUS: %s",cur->status);
            printf("\n\nCLOSE DATE: %d",cur->close_date);
        }
        cur=cur->next;
    }
    if (cur->next==NULL)
    {
        if (strcmp(key,cur->crime)==0)
        {
            printf("\n\n\n\n\tCIN: %d",cur->CIN);
            printf("\n\nSTART DATE: %d",cur->start_date);
            printf("\n\nNAME OF DEFENDANT: ");
            printf("%s",cur->defendants_name);
            printf("\n\nADDRESS OF DEFENDANT: %s",cur->defendants_address);
            printf("\n\nCRIME: %s",cur->crime);
            printf("\n\nNAME OF LAWYER: %s",cur->lawyers_name);
            printf("\n\nNAME OF PROSECUTOR: %s",cur->prosecutors_name);
            printf("\n\nNAME OF JUDGE: %s",cur->judges_name);
            printf("\n\nSTATUS: %s",cur->status);
            printf("\n\nCLOSE DATE: %d\n\n",cur->close_date);
        }
    }

    file_views++;
}

void browse_old_files()
{
    do
    {
        int choice;
        printf("\n1.Search by CIN\n2. Search by keyword\n\nChoose your option:  ");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1: search_by_cin();
                    exit(0);

            case 2: search_by_keyword();
                    exit(0);

            default: printf("\nEnter a valid option!");
        }
    }while (1);
}

void print_ongoing()
{
    char key[]="ongoing";
    node *cur=head;
    while(cur->next!=NULL)
    {
        if (strcmp(key,cur->status)==0)
        {
            printf("\n\n\n\n\tCIN: %d",cur->CIN);
            printf("\n\nSTART DATE: %d",cur->start_date);
            printf("\n\nNAME OF DEFENDANT: ");
            printf("%s",cur->defendants_name);
            printf("\n\nADDRESS OF DEFENDANT: %s",cur->defendants_address);
            printf("\n\nCRIME: %s",cur->crime);
            printf("\n\nNAME OF LAWYER: %s",cur->lawyers_name);
            printf("\n\nNAME OF PROSECUTOR: %s",cur->prosecutors_name);
            printf("\n\nNAME OF JUDGE: %s",cur->judges_name);
            printf("\n\nSTATUS: %s",cur->status);
            printf("\n\nCLOSE DATE: %d",cur->close_date);
        }
        cur=cur->next;
    }
    if (cur->next==NULL)
    {
        if (strcmp(key,cur->status)==0)
        {
            printf("\n\n\n\n\tCIN: %d",cur->CIN);
            printf("\n\nSTART DATE: %d",cur->start_date);
            printf("\n\nNAME OF DEFENDANT: ");
            printf("%s",cur->defendants_name);
            printf("\n\nADDRESS OF DEFENDANT: %s",cur->defendants_address);
            printf("\n\nCRIME: %s",cur->crime);
            printf("\n\nNAME OF LAWYER: %s",cur->lawyers_name);
            printf("\n\nNAME OF PROSECUTOR: %s",cur->prosecutors_name);
            printf("\n\nNAME OF JUDGE: %s",cur->judges_name);
            printf("\n\nSTATUS: %s",cur->status);
            printf("\n\nCLOSE DATE: %d\n\n",cur->close_date);
        }
    }
}

void upcoming_cases()
{
    do
    {
        int choice;
        printf("\n1.Print All Ongoing cases  2.Search by CIN  3.Search by keyword\n\nChoose your option:  ");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1: print_ongoing();
                    exit(0);

            case 2: search_by_cin();
                    exit(0);

            case 3: search_by_keyword();
                    exit(0);

            default: printf("\nEnter a valid option!");
        }
    }while (1);
}

//resolved upcoming pending
void sort_files()//only for registrar
{
    do
    {
        int choice;
        printf("\n\nSORT BY 1.Closed Cases  2.Ongoing cases\n\nChoose your option:  ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1: browse_old_files();
                    exit(0);

            case 2: upcoming_cases();
                    exit(0);

            default: printf("\nEnter a valid option!");
        }
    }while(1);
}

void check_status()
{
    int cin;
    printf("\nEnter CIN: ");
    scanf("%d", &cin);

    node *cur=head;
    while(cur->CIN!=cin)
    {
        cur=cur->next;
    }

    printf("\nSTATUS: %s\n\n", cur->status);
}

/*int main()
{
    create();
    //search_by_cin();
    //search_by_keyword();
    check_status();
}*/

