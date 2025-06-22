
// console.log("UserPermission", sessionStorage.getItem("UserPermissionJson"))

var selectedLanguage = "";
var selectedFont = "";
var newLineHeight = "";
var newLetterSpacing = "";
var fontSize = "";
var translations = "";
var currentPage = "";
var translations = "";

 function csvToJson(csv) {
  const lines = csv.split('\n');
  const headers = lines[0].split(',').map(header => header.trim());
  const result = [];

  for (let i = 1; i < lines.length; i++) {
    const obj = {};
    let values = [];
    let inQuotes = false;
    let currentValue = '';

    for (let char of lines[i]) {
      if (char === '"') {
        inQuotes = !inQuotes;
      } else if (char === ',' && !inQuotes) {
        values.push(currentValue.trim());
        currentValue = '';
      } else {
        currentValue += char;
      }
    }
    values.push(currentValue.trim()); // Push the last value

    if (values.length === headers.length) {
      for (let j = 0; j < headers.length; j++) {
        obj[headers[j]] = values[j];
      }
      result.push(obj);
    }
  }
  return result;
}


//  function  loadData() {
//   fetch("static/Common/MultiLang.csv").then(data => data.text()
//   ).then(data => {
//     const jsonTranslations = csvToJson(data);
//      translations = jsonTranslations;
//     // translations = data;
//   });
// }

async function loadData() {
  try {
    const response = await fetch("static/Common/MultiLang.csv");
    const data = await response.text();
    translations = csvToJson(data); // Assuming csvToJson is defined elsewhere
    console.log("Data loaded successfully!"); // Optional: Confirmation
  } catch (error) {
    console.error("Error loading data:", error);
  }
}

// loadData();

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



function toggleNavDrawer() {
  var navDrawer = document.getElementById('navDrawer');
  var overlay = document.getElementById('overlay');
  navDrawer.classList.toggle('open');
  overlay.style.display = navDrawer.classList.contains('open') ? 'block' : 'none';
  if (navDrawer.classList.contains('open')) {
    // Highlight the initially selected font size button when the drawer is opened
    var selectedSize = document.querySelector('.font-sizes .font-icon.selected-icon');
    if (selectedSize) {
      selectedSize.classList.remove('selected-icon');
    }
    selectedFont = sessionStorage.getItem(currentUser + '-FontSize')
    if (selectedFont == null)
      selectedFont = "small";

    var initialSize = document.querySelector('.font-sizes .font-icon[data-size="' + selectedFont + '"]');
    initialSize.classList.add('selected-icon');
  }
}

function closeNavDrawer() {
  var navDrawer = document.getElementById('navDrawer');
  var overlay = document.getElementById('overlay');
  navDrawer.classList.remove('open');
  overlay.style.display = 'none';
}
function loadCSV(path, callback) {
  fetch(path)
    .then(response => response.text())
    .then(data => callback(data))
    .catch(error => console.error('Error loading the CSV file:', error));
}

function tenantHandler(){
  debugger
  let sTenant=document.getElementById("tenantSelect").value
  if(sTenant!=localStorage.getItem('currentTenant')){
  localStorage.setItem('currentTenant',sTenant)
  location.reload()
  }
  sTenant=localStorage.getItem('currentTenant')
  let sLang = document.getElementById("languageSelect").value;
  changeLanguage("label",sLang,sTenant,window.location.pathname.split("/")[1]);
  prevLanguage = sLang;
  insertTelemetry(EVENT_SOURCE_SPECTRA, MASTERHEADER_LOAD_TENANT_SETTINGS, "Tenant Loaded successfully", JSON.stringify({ "Tenant": sTenant  }));

}

 function changeLanguage(prevLanguage, selectedLanguage, tenantName, pageName) {
  console.log(prevLanguage, selectedLanguage, tenantName, pageName)
  var reqTenantData = translations.filter(x => x.tenant == tenantName && (x.page_name == pageName || x.page_name == ""));
  var freeData = translations.filter(x => x.tenant == "");
  reqTenantData.push(...freeData);
  console.log(reqTenantData)
  reqTenantData.forEach(rt => {
    if (rt.label_type == "text") {
      // let reqPage = document.getElementById("child-content");
      // reqPage.innerHTML = reqPage.innerHTML.replace(rt.prevLanguage,rt.selectedLanguage);
    }
    else if (rt.label_type == "id") {
      console.log(rt.label_id,rt[selectedLanguage])
      document.getElementById(rt.label_id).innerText = rt[selectedLanguage];
    }
    else if(rt.label_type == "class"){
      // debugger
      let reqClassEle = document.querySelectorAll("."+rt.label_id);
      reqClassEle.forEach(e=>{
        
        if(e.innerHTML.includes(rt[prevLanguage])){
          e.innerHTML = e.innerHTML.replace(rt[prevLanguage],rt[selectedLanguage]);
        }
      })
    }
  });
  closeNavDrawer();
}


function changeModalText(id,selectedLanguage, tenantName, pageName) {
  console.log(prevLanguage, selectedLanguage, tenantName, pageName)
  var reqTenantData = translations.filter(x => x.tenant == tenantName && (x.page_name == pageName || x.page_name == ""));
  var freeData = translations.filter(x => x.tenant == "");
  reqTenantData.push(...freeData);
  console.log(reqTenantData)
  reqTenantData.forEach(rt => {
    // console.log(reqTenantData)
    if (rt.label_id == id) {
      console.log(rt.label_id, id)
      document.getElementById(id).innerText = rt[selectedLanguage];
      console.log(rt[selectedLanguage])
    }
    
  });
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

function changeLanguageByClass(selectedLanguage, cssclass, textValue) {
  let gridHeader = document.querySelectorAll(cssclass);
  // console.log(gridHeader)
  gridHeader.forEach(ele => {
    // // console.log(ele.innerText + selectedLanguage)
    // newLineHeight = sessionStorage.getItem(currentUser + '-LineHeight');
    // newLetterSpacing = sessionStorage.getItem(currentUser + '-LetterSpacing');
    // ele.style.fontSize = fontSize;
    // // // console.log(fontSize,newLineHeight,newLetterSpacing)
    // ele.style.lineHeight = newLineHeight;
    // ele.style.letterSpacing = newLetterSpacing;
    var label_id = ele.innerText
    if (label_id != "") {
      try {
        // // console.log(label_id, selectedLanguage, translations, translations[label_id][selectedLanguage])
        ele.innerText = textValue;
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
