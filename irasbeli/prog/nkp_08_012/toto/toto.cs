using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Toto
{
    class toto
    {
        struct Merkozes
        {
            public string csapat1;
            public string csapat2;
            public int gol1;
            public int gol2;
        }

        //4. feladat
        public static char x12(int gol1, int gol2)
        {
            if (gol1 > gol2)
                return '1';
            else if (gol2 > gol1)
                return '2';
            else
                return 'X';
        }
        public static int Meccsgeneralo(int csapatokszama, List<int> maralistabanvan)
        {
            Random veletlen = new Random();
            int generalt = veletlen.Next(0, csapatokszama);
            while (maralistabanvan.IndexOf(generalt) >= 0)
                generalt = veletlen.Next(0, csapatokszama);
            return generalt;
        }

        public static int Golkulonbseg(int gol1, int gol2)
        {
            return Math.Abs(gol1 - gol2);
        }

        static void Main(string[] args)
        {
            List<Merkozes> eredmenyek = new List<Merkozes>();

            //2. feladat
            Merkozes egymerkozes = new Merkozes();
            Console.Write("Adja meg a két csapat nevét kötőjellel elválasztva: ");
            string[] csapatok = Console.ReadLine().Split('-');
            egymerkozes.csapat1 = csapatok[0];
            egymerkozes.csapat2 = csapatok[1];

            //3. feladat
            Console.Write("Adja meg az eredményt kettősponttal elválasztva: ");
            string[] eredmeny= Console.ReadLine().Split(':');
            egymerkozes.gol1 = Convert.ToInt32(eredmeny[0]);
            egymerkozes.gol2 = Convert.ToInt32(eredmeny[1]);

            //5. feladat
            List<string> csapatnevek = new List<string>(File.ReadAllLines("csapatnevek.txt"));

            //6. feladat

            Random veletlen = new Random();
            List<int> veletlencsapat = new List<int>();
            for (int i = 0; i < csapatnevek.Count/2; i++)
            {
                Merkozes merkozes;
                int index = Meccsgeneralo(csapatnevek.Count, veletlencsapat);
                merkozes.csapat1 = csapatnevek[index];
                veletlencsapat.Add(index);
                index = Meccsgeneralo(csapatnevek.Count, veletlencsapat);
                merkozes.csapat2 = csapatnevek[index];
                veletlencsapat.Add(index);
                merkozes.gol1 = veletlen.Next(0, 6);
                merkozes.gol2 = veletlen.Next(0, 6);
                eredmenyek.Add(merkozes);
            }
            eredmenyek.Add(egymerkozes);

            //7. feladat
            StreamWriter sw = new StreamWriter("szelveny.txt");
            Console.WriteLine("Gergelyiugornyai totó 53. hét, telitalálatos szelvény:");
            sw.WriteLine("Gergelyiugornyai totó 53. hét, telitalálatos szelvény:");
            List<int> golkulonbsegek = new List<int>();
            foreach (var egymeccs in eredmenyek)
            {
                string egysor = egymeccs.csapat1 + " - " + egymeccs.csapat2 + "\t" + 
                                egymeccs.gol1 + ":" + egymeccs.gol2 + "\t" + 
                                x12(egymeccs.gol1, egymeccs.gol2);
                Console.WriteLine(egysor);
                sw.WriteLine(egysor);
                golkulonbsegek.Add(Golkulonbseg(egymeccs.gol1, egymeccs.gol2));
            }
            sw.Close();

            //8. feladat
            int maxgol = golkulonbsegek.Max();
            Console.Write("\r\nLegnagyobb gólkülönbségű mérkőzések: ");
            for (int i = 0; i < golkulonbsegek.Count; i++)
            {
                if (maxgol == golkulonbsegek[i])
                {
                    if (i != 7)
                        Console.Write(" {0}", i + 1);
                    else
                        Console.Write(" +1");
                }
            }
            Console.Write("\r\n0:0-ás mérkőzések: ");
            int db = 0;
            for (int i = 0; i < eredmenyek.Count; i++)
            {
                if (eredmenyek[i].gol1 == 0 && eredmenyek[i].gol2 == 0)
                {
                    if (i != 7)
                        Console.Write(" {0}", i + 1);
                    else
                        Console.Write(" +1");
                    db++;
                }
            }
            if (db == 0)
                Console.WriteLine("Nem volt 0:0-ás mérkőzés.");

            //9. feladat
            Console.Write("\r\nLegalább 2 gólos különbséggel nyertek: ");
            db = 0;
            for (int i = 0; i < golkulonbsegek.Count; i++)
            {
                if (golkulonbsegek[i] >= 2)
                {
                    string csapatnev = "";
                    if (x12(eredmenyek[i].gol1, eredmenyek[i].gol2) == '1')
                        csapatnev = eredmenyek[i].csapat1;
                    else
                        csapatnev = eredmenyek[i].csapat2;
                    if (db == 0)
                        Console.Write(" {0}", csapatnev);
                    else
                        Console.Write(", {0}", csapatnev);
                    db++;
                }
            }
            if (db == 0)
                Console.WriteLine("Nem volt legalább két gólos győzelem.");

           

        }
    }
}
