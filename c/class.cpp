#include "iostream"

using namespace std;

class User
{
public:
	User() 
	{
		cout<<"class created"<<endl;
	}

	// void printMe()
	virtual void printMe()
	{
		cout<<"About the User"<<endl;	
	}

	~User()
	{
		cout<<"class destroyed"<<endl;	
	}
};


class Teacher : public User
{
public:
	Teacher() 
	{
		cout<<"Teacher class created"<<endl;
	}

	void printMe()
	{
		cout<<"About the Teacher"<<endl;	
	}

	~Teacher()
	{
		cout<<"Teacher class destroyed"<<endl;	
	}
};

class Student : public User
{
public:
	Student() 
	{
		cout<<"Student class created"<<endl;
	}

	void printMe()
	{
		cout<<"About the Student"<<endl;	
	}

	~Student()
	{
		cout<<"Student class destroyed"<<endl;	
	}
};


int main(int argc, char const *argv[])
{
	User * u = new Teacher();
	u->printMe();

	return 0;
}