#include <cstring>
#include <iostream>

using namespace std;


bool resize_ref(int *&src_arr, size_t old_l, size_t new_l) {
	for (int i = 0 ; i < old_l ; i++) {
		cout << src_arr[i] << endl;
	}

	int* new_arr = new int[new_l];
	memcpy(new_arr, src_arr, old_l*sizeof(int));
	for (int i = old_l ; i < new_l ; i++) {
		new_arr[i] = (i+1)*(-10) ;
	}

	delete[] src_arr;
	src_arr = new_arr;
	return true;
}


int* resize(int *src_arr, size_t old_l, size_t new_l) {
	for (int i = 0 ; i < old_l ; i++) {
		cout << src_arr[i] << endl;
	}

	int* new_arr = new int[new_l];
	memcpy(new_arr, src_arr, old_l*sizeof(int));
	for (int i = old_l ; i < new_l ; i++) {
		new_arr[i] = (i+1)*(-10) ;
	}
	delete[] src_arr;
	return new_arr;
}


int main(int argc, const char *argv[]) {
	int* a = new int[5];
	for (int i = 0 ; i < 5 ; i++) {
		a[i] = (i+1)*10;
	}

	// int* b = resize(a, 5, 10);
	// for (int i = 0 ; i < 10 ; i++) {
	// 	cout << b[i] << endl;
	// }	

	bool ret = resize_ref(a, 5, 10);
	for (int i = 0 ; i < 10 ; i++) {
		cout << a[i] << endl;
	}	

}