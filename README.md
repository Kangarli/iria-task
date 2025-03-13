
# Python Test Avtomatlaşdırma

Burada məqsəd, **Python** istifadə edərək bir vebsaytın əsas istifadəçi interfeysi (UI) testlərini avtomatlaşdırmaq və test infrastrukturu qurmaq idi. **Selenium**, **Behave** (Cucumber-in Python versiyası) istifadə edilmişdir.

---

## Məqsədi

Bu layihə, verilmiş bir tapşırığın yerinə yetirilməsi üçün hazırlanmışdır və aşağıdakı hədəflərə malikdir:
1. Form göndərmə, dinamik elementlərlə və cədvəllərlə işləmə UI testlərini avtomatlaşdırmaq.  
2. Modulyar bir test infrastrukturu quraraq təkrarlana bilən və genişlənə bilən bir çərçivə yaratmaq.  
3. Testlərdən sonra HTML hesabatları yaratmaq və uğursuz testlər üçün ekran görüntülərini saxlamaq.  

---

## Fayl Strukturu

Layihənin fayl strukturu aşağıdakı kimidir:

```
README.md       generate_html.py    pages           screenshots     utils
features        iriavenv        reports         tree_requirements.txt

./features:
dynamic_controls.feature    environment.py          form_validation.feature     steps               table_extraction.feature

./features/steps:
common_steps.py         dynamic_controls_steps.py   form_validation_steps.py    table_extraction_steps.py

./pages:
base_page.py    dynamic_page.py form_page.py    table_page.py

./reports:
report.html results.json

./screenshots:
2025-03-12  2025-03-13

./utils:
csv_reader.py   driver_setup.py screenshot.py
```

### Qovluqların İzahı:
- **features:** Test ssenarilərini təsvir edən `.feature` fayllarını və testlərin icrası üçün lazım olan dəstək fayllarını saxlamaq üçündür.  
- **features/steps:** Test ssenarilərindəki addımlara uyğun gələn Python fayllarını saxlayır.  
- **pages:** **Page Object Model (POM)** strukturuna uyğun hazırlanmış səhifələr, (kod daxilində səhifələrin testləri olmayıb, lakin edildiyi halda burda əlavə ediləcək).
- **reports:** Test nəticələrinin ətraflı şəkildə qeyd olunduğu HTML və JSON hesabatlar.  
- **screenshots:** Uğursuz test addımları zamanı alınan ekran görüntüləri.  
- **utils:** İstifadə olumuş digər funksiyalar
---

## Necə İstifadə Edilir?

### Tələblər
- Python 3.8 və ya daha yüksək versiya  
- Lazımi Python kitabxanaları (`pip install` ilə quraşdırıla bilər)  
- Selenium WebDriver  

### Quraşdırma
1. Layihəni yükləyin:
   ```bash
   git clone https://github.com/Kangarli/iria-task.git
   cd iria-task
   ```
2. Virtual Python mühiti yaradın və aktivləşdirin:
   ```bash
   python -m venv iriavenv
   source iriavenv/bin/activate
   ```
3. Lazımi kitabxanaları quraşdırın:
   ```bash
   sudo pip install -r tree_requirements.txt
   ```

### Testləri İşə Salma
Test ssenarilərini işlətmək üçün aşağıdakı əmri icra edin:
```bash
behave
```
Test nəticələrini json olaraq saxlamaq üçün:
```bash
behave --format json --outfile reports/results.json
```
Test nəticələrini HTML olaraq saxlamaq üçün:
```bash
behave -f html -o reports/report.html
```
Bəziən lokal konfigurasiyaya əsasən behave html yarada bilməsə əlavə funksiya ilə yaratmaq olar
```bash
python generate_html.py
```

### Hesabat və Ekran Görüntüləri
- Test nəticələri **./reports** qovluğundakı `report.html` faylında saxlanır.  
- Uğursuz olan testlər üçün alınan ekran görüntüləri **./screenshots** qovluğuna qeyd olunur.  

---

## Avtomatlaşdırılmış Test Ssenariləri

### 1. Form
**Məqsəd:** Form girişlərini doğru və yanlış verilərlə test edərək yoxlamaq.  
**Tapşırıqlar:**
- Formu doğru və yanlış məlumatlarla doldurmaq və göndərmək.  
- Səhv girişlər üçün xəta mesajlarını yoxlamaq.  
- Uğurlu göndərişlər üçün success mesajını yoxlamaq.  

### 2. Dinamik inputlar
**Məqsəd:** Dinamik UI elementləri ilə işləmək.  
**Tapşırıqlar:**
- Görünən və yox olan checkbox-ları idarə etmək.  
- İnputları aktiv/deaktiv etmək və onları yoxlamaq.  

### 3. Cədvəllər
**Məqsəd:** Cədvəllər ilə işləmək.  
**Tapşırıqlar:**
- Cədvəldəki məlumatları və butonları yoxlamaq.  
- Əməliyyat öncəsi və sonrası sətr sayını yoxlamaq.  
- Cədvəlin sıralama qaydasını yoxlamaq (artan/azalan).  

---

## Qeydlər
- Bu layihə tapşırığın icrası üçün hazırlanmışdır və istifadə edilən texnologiyalar ilə səmərəli bir test infrastruktur qurmağa çaılşmışam.  
- Hesabatlar test prosesi haqqında dəqiq məlumatlar verir, ekran görüntüləri isə xətaları təhlil etməyi asanlaşdırır.  

**GitHub Link:** iria-task [https://github.com/Kangarli/iria-task.git]

#### -- kod hər zaman daha yaxşı yazıla bilər --