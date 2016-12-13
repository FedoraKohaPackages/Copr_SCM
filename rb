directory=$(pwd)
mkdir BUILD
cd BUILD
mkdir SOURCES
cp ../*gz SOURCES
cp ../*patch SOURCES
rpmbuild --define "_topdir `pwd` " -bs --nodeps  ../*.spec
cp SRPMS/*.rpm ../
cd ..
rm -rf BUILD
srpm=$(ls *.src.rpm)
git add *.rpm
git commit -m "New SRPM for $srpm"
git push
copr-cli build KOHAExtra https://raw.githubusercontent.com/FedoraKohaPackages/Copr_SCM/master/$directory/$srpm
