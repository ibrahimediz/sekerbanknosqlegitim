"""
SELECT 
isim,
count(islemtipi) as islemsayisi
FROM 
kayitlar
WHERE isim = 'tamamlandi'
group by isim
order by islemsayisi
"""
