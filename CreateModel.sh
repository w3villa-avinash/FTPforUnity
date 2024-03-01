# bash
RED="\e[31m"
GREEN="\e[32m"
BLUE="\e[34m"
CYAN="\e[36m"
GRAY="\e[90m"
ENDCOLOR="\e[0m"

#=============================> Run Terminal Commands <=============================
while getopts "d:o:f:p:h" flag
do
    case "${flag}" in
        d) detail=${OPTARG};;
        o) sampleOrdering=${OPTARG};;
        f) featureSensitivity=${OPTARG};;
        p) folderPath=${OPTARG};;
        # h) helpW=${OPTARG};;
    esac
done

# if [[ "$1" == ' ' ]]; then
# if [ "$#" -eq 0 ] && [ -n "$1" ] && [ -n "$2" ] && [ -n "$3" ]; then
show_help()
{
echo "
    OPTIONS:
        -d,                     <detail>
                                Detail {preview, reduced, medium, full, raw}  Detail
                                of output model in terms of mesh size and texture
                                 size. (default: nil)
        -o,                     <sample-ordering>
                                 SampleOrdering {unordered, sequential}  Setting to
                                sequential may speed up computation if images are
                                captured in a spatially sequential pattern.
        -f,                     <feature-sensitivity>
                                featureSensitivity {normal, high}  Set to high if the
                                scanned object does not contain a lot of discernible
                                structures, edges or textures.
        -p,                     <path>
                                Path to the folder containing the Images
        -h, --help              Show help information.
"
}

# # if [ "$1" == '-h' ] || [ "$3" == '-h' ] || [ "$5" == '-h' ] || [ "$3" == '-h' ]; then
# if [[ $* == *-h* ]] ; then
#     show_help
#     exit 0
# fi

# #Bash also takes the flags as argument count. Ex: -d | -o
# if [ "$#" -le 6 ] ; then
#     printf "Provide all arguments\n"
#     exit 0
# # else
# #     printf "First argument '$1' provided"
# fi

printf "\n$GRAY Passed Arguments $ENDCOLOR"
printf "\n\t-$CYAN Detail Selected $ENDCOLOR:$GREEN $detail $ENDCOLOR"
printf "\n\t-$CYAN Sample Ordering $ENDCOLOR:$GREEN $sampleOrdering $ENDCOLOR"
printf "\n\t-$CYAN Sample Ordering $ENDCOLOR:$GREEN $featureSensitivity $ENDCOLOR\n"
# exit          #Test command

printf "\n$BLUE Beginning to Create Mesh... $ENDCOLOR\n"
# pwd

#Create New Folder to store the model
printf "\n$GRAY Making New Folder... $ENDCOLOR"
createDir="Output"
rm -rf ./$createDir
mkdir $createDir
createSubDir="Test_Scan"
createdDirPath="./$createDir/$createSubDir"
mkdir $createdDirPath

#Name of Model
printf "\n$GRAY Assigning Name to Mesh... $ENDCOLOR\n"
newModelName="Bash_Test_Model_01"
# exit          #Test command

#Call Photogrammetry Api
printf "\n$GREEN Creating Mesh... \n"
output_path="/Users/apple/Documents/Python/LocalData/Output/"
./HelloPhotogrammetry "/Users/apple/Documents/Python/LocalData/Input" $output_path/$newModelName.usdz -d "medium" -o "unordered" -f "normal"
# rm -rf $createdDirPath             #Clear the cache