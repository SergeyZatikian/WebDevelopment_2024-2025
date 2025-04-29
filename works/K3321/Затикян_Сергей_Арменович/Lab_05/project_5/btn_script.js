document.addEventListener('DOMContentLoaded', function() {
    const districtDisplay = document.getElementById('district-display');
    const image = document.getElementById('erevan-img');
    const districtBtns = document.querySelectorAll('.district-btn');
    
    // Инициализация карты после загрузки изображения
    image.onload = function() {
        initMapAreas();
        initDistrictButtons();
    };
    
    if (image.complete) {
        initMapAreas();
        initDistrictButtons();
    }
    
    function initMapAreas() {
        const areas = document.querySelectorAll('map area');
        
        areas.forEach(area => {
            area.addEventListener('mouseenter', function() {
                showDistrictInfo(this.dataset.name, this.dataset.description);
            });
        });
    }
    
    function initDistrictButtons() {
        districtBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const districtName = this.dataset.district;
                const area = document.querySelector(`area[data-name="${districtName}"]`);
                
                if (area) {
                    showDistrictInfo(area.dataset.name, area.dataset.description);
                }
            });
        });
    }
    
    function showDistrictInfo(name, description) {
        districtDisplay.innerHTML = `
            <div class="district-name">${name}</div>
            <div class="district-description">${description}</div>
        `;
    }
});