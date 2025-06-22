
    // console.log("UserPermission", sessionStorage.getItem("UserPermissionJson"))
   
    var selectedLanguage = "";
    var selectedFont = "";
    var newLineHeight = "";
    var newLetterSpacing = "";
    var fontSize = "";
    var translations = "";
    var currentPage = "";
    var translations = "";

    function loadData() {
      fetch("static/Common/MultiLang.csv").then(data => data.text()
      ).then(data => {
        const jsonTranslations = csvJSON(data);
        translations = JSON.parse(jsonTranslations);
      });
    }
    loadData();

    console.log('document.getElementById("languageSelect")')
    
    function changeFontSize(size) {
      sessionStorage.setItem(currentUser + '-FontSize', size);
      selectedFont = sessionStorage.getItem(currentUser + '-FontSize');
      var fontSizeOptions = {
        small: '14px',
        medium: '16px',
        large: '20px'
      };
      fontSize = fontSizeOptions[size];

      document.body.style.fontSize = fontSize;
      // console.log("---------->>>>>>", size, fontSize, window.getComputedStyle(document.body).getPropertyValue('font-size'), sessionStorage.getItem(currentUser + '-FontSize'))

      // Highlight selected icon
      var fontIcons = document.querySelectorAll('.font-icon');
      fontIcons.forEach(function (icon) {
        icon.classList.remove('selected-icon');
      });
      // sessionStorage.setItem(currentUser + '-FontSize', size)
      var selectedIcon = document.querySelector('.font-icon[data-size="' + size + '"]');
      selectedIcon.classList.add('selected-icon');
      closeNavDrawer(); // Close the navigation drawer after selecting a font size
    }

    function csvJSON(csv) {
      var lines = csv.split("\n");
      var result = {};
      var headers = lines[0].split(",");
      // console.log(headers)
      for (var i = 1; i < lines.length; i++) {
        var obj = {};
        var currentline = lines[i].split(",");
        for (var j = 1; j < headers.length; j++) {
          obj[headers[j]] = currentline[j];
        }
        result[currentline[0]] = obj;
      }
      return JSON.stringify(result, null, 4);
    }

    function loadCSV(path, callback) {
      fetch(path)
        .then(response => response.text())
        .then(data => callback(data))
        .catch(error => console.error('Error loading the CSV file:', error));
    }

    function changeLanguage(selectedLanguage) {
      // selectedLanguage = document.getElementById("languageSelect").value;
      sessionStorage.setItem(currentUser + '-Language', selectedLanguage)
      selectedLanguage = sessionStorage.getItem(currentUser + '-Language');
      // var translation = translations[selectedLanguage];

      // // console.log(translations, selectedLanguage)
      // // console.log(translation)

      // document.getElementById("header_text").innerText = translations.header_text[selectedLanguage];
      // document.getElementById("footer").innerText = translations.footer[selectedLanguage];

      document.getElementById("welcome_text").innerText = translations.welcome_text[selectedLanguage]+" - ";
      document.getElementById("networkLabel").innerText = translations.networkLabel[selectedLanguage];
      document.getElementById("navheadertext").innerText = translations.navheadertext[selectedLanguage];
    //   document.getElementById("navDdrawer_Accessibility").innerText = translations.navDdrawer_Accessibility[selectedLanguage];
      document.getElementById("navDdrawer_Accessibility").innerText = translations.navDdrawer_Accessibility[selectedLanguage];
      document.getElementById("navDdrawer_FontSize").innerText = translations.navDdrawer_FontSize[selectedLanguage];
      document.getElementById("navDdrawer_Language").innerText = translations.navDdrawer_Language[selectedLanguage];
      document.getElementById("navDdrawer_LineHeight").innerText = translations.navDdrawer_LineHeight[selectedLanguage];
      document.getElementById("navDdrawer_LetterSpacing").innerText = translations.navDdrawer_LetterSpacing[selectedLanguage];
      document.getElementById("navDdrawer_KeyboardNavigation").innerText = translations.navDdrawer_KeyboardNavigation[selectedLanguage];
      changeNavBarLanguage(translations, selectedLanguage, ".nav-link")
      changeNavBarLanguage(translations, selectedLanguage, ".dropdown-menu .dropdown-item")
      closeNavDrawer();

    }
    // function changeLanguage(translations, selectedLanguage) {
    //   // selectedLanguage = document.getElementById("languageSelect").value;
    //   sessionStorage.setItem(currentUser + '-Language', selectedLanguage)
    //   selectedLanguage = sessionStorage.getItem(currentUser + '-Language');
    //   // var translation = translations[selectedLanguage];

    //   // // console.log(translations, selectedLanguage)
    //   // // console.log(translation)

    //   // document.getElementById("header_text").innerText = translations.header_text[selectedLanguage];
    //   // document.getElementById("footer").innerText = translations.footer[selectedLanguage];

    //   document.getElementById("welcome_text").innerText = translations.welcome_text[selectedLanguage]+" - ";
    //   document.getElementById("networkLabel").innerText = translations.networkLabel[selectedLanguage];
    //   document.getElementById("navheadertext").innerText = translations.navheadertext[selectedLanguage];
    // //   document.getElementById("navDdrawer_Accessibility").innerText = translations.navDdrawer_Accessibility[selectedLanguage];
    //   document.getElementById("navDdrawer_Accessibility").innerText = translations.navDdrawer_Accessibility[selectedLanguage];
    //   document.getElementById("navDdrawer_FontSize").innerText = translations.navDdrawer_FontSize[selectedLanguage];
    //   document.getElementById("navDdrawer_Language").innerText = translations.navDdrawer_Language[selectedLanguage];
    //   document.getElementById("navDdrawer_LineHeight").innerText = translations.navDdrawer_LineHeight[selectedLanguage];
    //   document.getElementById("navDdrawer_LetterSpacing").innerText = translations.navDdrawer_LetterSpacing[selectedLanguage];
    //   document.getElementById("navDdrawer_KeyboardNavigation").innerText = translations.navDdrawer_KeyboardNavigation[selectedLanguage];
    //   changeNavBarLanguage(translations, selectedLanguage, ".nav-link")
    //   changeNavBarLanguage(translations, selectedLanguage, ".dropdown-menu .dropdown-item")
    //   closeNavDrawer();

    // }

    // Function to change line height dynamically
    function changeLineHeight(newLineHeight) {
      sessionStorage.setItem(currentUser + '-LineHeight', newLineHeight)
      newLineHeight = sessionStorage.getItem(currentUser + '-LineHeight');

      const icons = $('.font-sizes-line-height i');
      icons.removeClass('selected-icon');
      const selectedIcon = icons.filter(function () {
        return $(this).data('size') === newLineHeight;
      });
      selectedIcon.addClass('selected-icon');

      // Remove selected class from all links and add it to the clicked one
      $('.font-sizes-line-height a').removeClass('selected-link');
      selectedIcon.closest('a').addClass('selected-link');


      document.body.style.lineHeight = newLineHeight;

      closeNavDrawer(); // Close the navigation drawer after selecting a font size
    }

    // Function to change letter spacing dynamically
    function changeLetterSpacing(newLetterSpacing) {

      sessionStorage.setItem(currentUser + '-LetterSpacing', newLetterSpacing)
      newLetterSpacing = sessionStorage.getItem(currentUser + '-LetterSpacing');
      const icons = $('.font-sizes-letter-spacing i');
      icons.removeClass('selected-icon');
      const selectedIcon = icons.filter(function () {
        return $(this).data('size') === newLetterSpacing;
      });
      selectedIcon.addClass('selected-icon');

      // Remove selected class from all links and add it to the clicked one
      $('.font-sizes-letter-spacing a').removeClass('selected-link');
      selectedIcon.closest('a').addClass('selected-link');

      document.body.style.letterSpacing = newLetterSpacing;
      closeNavDrawer(); // Close the navigation drawer after selecting a font size
    }
    
    function changeNavBarLanguage(translations, selectedLanguage, cssClass) {
      // console.log(">>>>>>>>", translations, selectedLanguage, cssClass)
      let navItems = document.querySelectorAll(cssClass);
      navItems.forEach(ele => {
        var labelId = ele.id; // Get the text, trim any extra spaces
        if (labelId && translations[labelId] && translations[labelId][selectedLanguage]) {
          try {
            ele.innerText = translations[labelId][selectedLanguage];
          } catch (error) {
            console.error('Fetch error:', error);
          }
        }
      });
    }

    function changeLanguageByClass(innerDoc, translations, selectedLanguage, cssclass) {
      let gridHeader = innerDoc.querySelectorAll(cssclass);
      // console.log(gridHeader)
      gridHeader.forEach(ele => {
        // // console.log(ele.innerText + selectedLanguage)
        newLineHeight = sessionStorage.getItem(currentUser + '-LineHeight');
        newLetterSpacing = sessionStorage.getItem(currentUser + '-LetterSpacing');
        ele.style.fontSize = fontSize;
        // // console.log(fontSize,newLineHeight,newLetterSpacing)
        ele.style.lineHeight = newLineHeight;
        ele.style.letterSpacing = newLetterSpacing;
        var label_id = ele.innerText
        if (label_id != "") {
          try {
            // // console.log(label_id, selectedLanguage, translations, translations[label_id][selectedLanguage])
            ele.innerText = translations[label_id][selectedLanguage];
          }
          catch (error) {
            console.error(label_id, 'Fetch error:', error);
          }
        }
      });
    }

    function LineHeightChange(option) {
      // onChangeAccessibility("LineHeight", option);
      changeLineHeight(option);
      const pageName = window.location.hash.substring(1);
      if (pageName) {
        loadChildPage(pageName);
      }

    }

    function LetterSpacingChange(option) {
      if (sessionStorage.getItem(currentUser + '-FontSize') == 'large' && option != "-1px") {
        alert("Please Select a smaller Font Size to enable this setting")
      }
      else if (sessionStorage.getItem(currentUser + '-FontSize') == 'medium' && option == "1px") {
        alert("Please Select a smaller Font Size to enable this setting")
      }
      else {
        // onChangeAccessibility("LetterSpacing", option);
        changeLetterSpacing(option);
        const pageName = window.location.hash.substring(1);
        if (pageName) {
          loadChildPage(pageName);
        }
      }
    }
    console.log('document.getElementById("languageSelect")')
    function langchange() {
      selectedLanguage = document.getElementById("languageSelect").value;
      // onChangeAccessibility("Language", selectedLanguage);
      changeLanguage(translations, selectedLanguage);
      const pageName = window.location.hash.substring(1);
      if (pageName) {
        loadChildPage(pageName);
      }
    }

    function largeFont() {
      // onChangeAccessibility("FontSize", "large");
      changeFontSize("large")
      LetterSpacingChange("-1px")
      const pageName = window.location.hash.substring(1);
      if (pageName) {
        loadChildPage(pageName);
      }
    }

     function mediumFont() {
      // onChangeAccessibility("FontSize", "medium");
      changeFontSize("medium")
      const pageName = window.location.hash.substring(1);
      if (pageName) {
        loadChildPage(pageName);
      }
    }

    function smallFont() {
      // onChangeAccessibility("FontSize", "small");
      changeFontSize("small")
      const pageName = window.location.hash.substring(1);
      if (pageName) {
        loadChildPage(pageName);
      }
    };
