#include <iostream>

using namespace std;

/*
Nama     : Dhimas Aditya Sampoeha
Kelas    : TI.20.D2
NIM      : 312010224
*/

void trans(int b)
{
   if (b == 0)
   {
      cout << "Nol";
   }
   else if (b == 1)
   {
      cout << "Satu";
   }
   else if (b == 2)
   {
      cout << "Dua";
   }
   else if (b == 3)
   {
      cout << "Tiga";
   }
   else if (b == 5)
   {
      cout << "Lima";
   }
   else if (b == 8)
   {
      cout << "Delapan";
   }
   else if (b == 13)
   {
      cout << "Tiga Belas";
   }
   else if (b == 21)
   {
      cout << "Dua Puluh Satu";
   }
   else if (b == 34)
   {
      cout << "Tiga Puluh Empat";
   }
   else if (b == 55)
   {
      cout << "Lima Puluh Lima";
   }
   else if (b == 89)
   {
      cout << "Delapan Puluh Sembilan";
   }
   else if (b == 144)
   {
      cout << "Seratus Empat Puluh Empat";
   }
   else if (b == 233)
   {
      cout << "Dua Ratus Tiga Puluh Tiga";
   }
   else if (b == 377)
   {
      cout << "Tiga Ratus Tujuh Puluh Tujuh";
   }
   else if (b == 610)
   {
      cout << "Enam Ratus Sepuluh";
   }
   else if (b == 987)
   {
      cout << "Sembilan Ratus Delapan Puluh Tujuh";
   }
   else if (b == 1597)
   {
      cout << "Seribu Lima Ratus Sembilan Puluh Tujuh";
   }
   else if (b == 2584)
   {
      cout << "Dua Ribu Lima Ratus Delapan Puluh Empat";
   }
   else if (b == 4181)
   {
      cout << "Empat Ribu Seratus Delapan Puluh Satu";
   }
   else if (b == 6765)
   {
      cout << "Enam Ribu Tujuh Ratus Enam Puluh Lima";
   }
}
int main()
{
   //DeklarasI Variabel a b c n
   int a, b, c, n, no;
   a = 0;
   b = 1;
   c = 0;

   //Untuk Input Nilai Fibonacci
   cout << "Masukan Nilai Fibonacci : ";
   cin >> n;

   /*
   Jika Ingin Menggunakan 0 diawal
   trans(0);
   cout << "" << endl;
   */

   //Perulangan Untuk Fibonacci
   for (int i = 0; i < n; i++)
   {
      //Melakukan Cetak Result dengan Hasil dari memanggil Function Trans()
      cout << i << ". ";
      trans(b);
      //cout << " | ";
      cout << "" << endl;
      c = a + b;
      a = b;
      b = c;
   }

   return 0;
}
