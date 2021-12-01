#!/usr/bin/perl
$file = "../input";

print "--- Part One ---\n";
open $input_fh, '<', $file or die "Could not open $file: $!\n";

$count = 0;
$prev_value = <$input_fh>;
$value = <$input_fh>;
chop($prev_value);
chop($value);
while ($line = <$input_fh>) {
	if ($prev_value < $value) {
		$count++;
	}
	$prev_value = $value;
	$value = $line;
	chop($value);
}
if ($prev_value < $value) {
	$count++;
}
print "Result: ".$count." 'increased'\n";
close $input_fh or die "Failed to close $file: $!\n";
print "--- Part Two ---\n";

sub sum_array {
	my @array = @{$_[0]};
	my $sum = 0;
	foreach my $i (@array) {
		$sum += $i
	}
	return $sum;
}

open $input_fh, '<', $file or die "Could not open $file: $!\n";

$count = 0;
@window1 = (0, 0, 0);
$window1[0] = <$input_fh>;
chop($window1[0]);
$window1[1] = <$input_fh>;
chop($window1[1]);
$window1[2] = <$input_fh>;
chop($window1[2]);
@window2 = ($window1[1], $window1[2], 0);
$window2[2]=<$input_fh>;
chop($window2[2]);
while ($line = <$input_fh>) {
#	print "[".$window1[0].", ".$window1[1].", ".$window1[2]."] - ";
#	print "[".$window2[0].", ".$window2[1].", ".$window2[2]."]\n";
#	print sum_array(\@window1)." vs ".sum_array(\@window2)."\n";
	if (sum_array(\@window1) < sum_array(\@window2)) {
		$count++;
	}
	$window1[0] = $window1[1];
	$window1[1] = $window1[2];
	$window1[2] = $window2[2];
	$window2[0] = $window2[1];
	$window2[1] = $window2[2];
	$window2[2] = $line;
	chop($window2[2]);
}
if (sum_array(\@window1) < sum_array(\@window2)) {
	$count++;
}

print "Result: ".$count." 'increased'\n";
close $input_fh or die "Failed to close $file: $!\n";
