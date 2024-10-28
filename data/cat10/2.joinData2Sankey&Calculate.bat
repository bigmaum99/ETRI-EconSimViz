rem @echo off

rem echo Processing eco_sim_db_10cat.sankey - binding data, calculating, export to SVG, and save as _res.sankey

rem IF NOT EXIST output (
rem    MD output
rem )

rem eSankeyConsole.exe -updatevalues:"simulation-quarter-results-2015Q2-cat10-run40.txt" "eco_sim_db_10cat_v18.sankey" -initializeplugins -calculate "eco_sim_db_10cat_v18.sankey" -export:"eco_sim_db_10cat_v18.svg" -exporttype:svg -svgToolTipStyle:smart -svgEnableHighlightFlows -svgEnableMoveZoom "eco_sim_db_10cat_v18.sankey" 

rem rem -saveas:"eco_sim_db_10cat_res.sankey"
rem rem echo eSankeyConsole.exe -updatevalues:"eco_sim_db_10cat-data1.txt" selected_file -initializeplugins -calculate "eco_sim_db_10cat.sankey" -export:!filename!".svg" -exporttype:svg -svgToolTipStyle:smart -svgEnableHighlightFlows -svgEnableMoveZoom !selected_file! -saveas:!filename!"_res.sankey"


rem pause


@echo off
chcp 65001 >nul

echo Processing eco_sim_db_10cat_v18.sankey - binding data, calculating, export to SVG, and save as _res.sankey
echo.

setlocal enabledelayedexpansion

rem 폴더 내 txt 파일 목록 출력
echo 데이터 파일 목록:
set /a count=0
for %%f in (*.txt) do (
    set /a count+=1
    set "file[!count!]=%%f"
    set "filename[!count!]=%%~nf"
    rem echo !count!. %%~nf
    echo !count!. %%f
)

echo.
rem 사용자에게 번호 입력 받기
set /p choice=sankey 파일과 결합할 txt 파일 번호를 선택하세요:


if defined filename[%choice%] (
   set "data_file=!filename[%choice%]!.txt"
   set "sankey_file=eco_sim_db_10cat_v18.sankey"
   set "export_file=!filename[%choice%]!.svg"


   rem echo !data_file!
   rem echo !sankey_file!
   rem echo !export_file!

   rem eSankeyConsole 명령어 실행
   eSankeyConsole.exe -updatevalues:"!data_file!" "!sankey_file!" -initializeplugins -calculate "!sankey_file!" -export:"!export_file!" -exporttype:svg -svgToolTipStyle:smart -svgEnableHighlightFlows -svgEnableMoveZoom "!sankey_file!" 
   echo.
   echo sankey차트와 데이터 파일의 결합 처리가 완료되었습니다..
   echo !export_file!

) else (
   echo 잘못된 번호를 입력했습니다.
)




echo.
echo.



endlocal
pause
exit

