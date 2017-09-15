cat pos-1-162-16k.fa > pos-test.fa
cat pos-2-162-16k.fa > pos-valid.fa
cat pos-3-162-16k.fa pos-4-162-16k.fa pos-5-162-16k.fa > pos-train.fa

cat neg-1-139-162-5utr.txt neg-1-2622-162-cds.txt neg-1-872-162-intron.txt > neg-1-162.fa
cat neg-2-77-162-5utr.txt neg-2-1442-162-cds.txt neg-2-502-162-intron.txt > neg-2-162.fa
cat neg-3-101-162-5utr.txt neg-3-1899-162-cds.txt neg-3-594-162-intron.txt > neg-3-162.fa
cat neg-4-77-162-5utr.txt neg-4-1500-162-cds.txt neg-4-503-162-intron.txt > neg-4-162.fa
cat neg-5-107-162-5utr.txt neg-5-2241-162-cds.txt neg-5-751-162-intron.txt > neg-5-162.fa


cat neg-1-162.fa > neg-test.fa
cat neg-2-162.fa > neg-valid.fa
cat neg-3-162.fa neg-4-162.fa neg-5-162.fa > neg-train.fa
