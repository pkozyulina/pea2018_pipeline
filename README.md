# pea2018_pipelin

Последовательность действий:

0) Установить RSEM, Snakemake и bedtools согласно инструкциям:

https://github.com/deweylab/RSEM

https://snakemake.readthedocs.io/en/stable/getting_started/installation.html

sudo apt-get install bedtools
(https://bedtools.readthedocs.io/en/latest/content/installation.html)

1) создать индекс для bowtie2 и RSEM:

bowtie2-build -f /PATHTOREFERENCE/GDTM01.1.filtered.fsa_nt /PATHTOREFERENCE/PisumSativum_bwt

rsem-prepare-reference /PATHTOREFERENCE/GDTM01.1.filtered.fsa_nt /PATHTOREFERENCE/PisumSativum_rsem

2) Скопировать все bam файлы в отдельную директорию

3) Запустить скрипт для создания .json файла:

/PATHTOCRIPT/generate_json.py

4) Проверить наличие файла 'rsem.json' в рабочей директории

5) Прописать в текстовоv файле /PATHTOCRIPT/preprocessing.snakefile абсолютные пути для следующих констант:

RSEMREF = '/home/pkozyulina/reference/PisumSativum' (путь до референса, созданного RSEM)
BWT2REF = '/home/pkozyulina/reference/PisumSativum_bwt'(путь до референса, созданного bowtie2)
PATHTOBOWTIE2 = '/home/pkozyulina/TOOLS/bowtie2-2.3.4.1-linux-x86_64/' (путь до папки с исполняющим файлом bowtie2)
PATHTORSEM = '/home/pkozyulina/TOOLS/RSEM-1.3.1'(путь до папки с исполняющим файлом RSEM)
THREADS = 8 (указать имеющееся число ядер - если есть возможность распараллелить задачи и сократить время расчетов)

6) Запустить проверку пайплайна при помощи команды:

snakemake -s /PATHTOCRIPT/preprocessing.snakefile --configfile rsem.json -np

Если все было сделано верно, то в терминал должен быть выведен список файлов и задач (обозначенных желтым и зеленым цветом). Не должно появиться надписей типа error и красного цвета.

7) Запустить пайплайн в работу при помощи команды:

snakemake -s /PATHTOCRIPT/preprocessing.snakefile --configfile rsem.json --cores CORES_NUMBER 
, где CORES_NUMBER - количество ядер для распараллеливания

