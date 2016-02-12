#include "iostream"
#include "fstream"

using namespace std;

int main(int argc, char const *argv[])
{
	/* code */
	string fileName = "./class.cpp";
	cout << fileName << endl;
	std::ifstream ifs (fileName.c_str(), std::ifstream::in);
	ifs.seekg (7, ifs.beg);
	std::string line;
	while (std::getline(ifs, line))
	{
		std::cout << line << std::endl;
	}
	return 0;
}