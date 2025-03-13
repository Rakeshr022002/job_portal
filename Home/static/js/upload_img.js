 let profile_Pic = document.getElementById("profile-pic")
let Input_File  = document.getElementById("input-file")



Input_File.onchange = function(){
    profile_Pic.src = URL.createObjectURL(Input_File.files[0]);
}



let institute_Pic = document.getElementById("ins-pic")
let institute_file = document.getElementById("ins-file")

institute_file.onchange = function () {
    institute_Pic.src = URL.createObjectURL(institute_file.files[0]);
}