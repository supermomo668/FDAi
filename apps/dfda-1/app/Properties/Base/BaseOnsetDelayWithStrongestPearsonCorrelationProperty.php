<?php
/*
*  GNU General Public License v3.0
*  Contributors: ADD YOUR NAME HERE, Mike P. Sinn
 */

namespace App\Properties\Base;
use App\Traits\PropertyTraits\IsInt;
use App\UI\ImageUrls;
use App\UI\FontAwesome;
use App\Properties\BaseProperty;
class BaseOnsetDelayWithStrongestPearsonCorrelationProperty extends BaseProperty{
	use IsInt;
	public $dbInput = 'integer,false';
	public $dbType = \Doctrine\DBAL\Types\Types::INTEGER;
	public $default = \OpenApi\Generator::UNDEFINED;
	public $description = 'onset_delay_with_strongest_pearson_correlation';
	public $fieldType = self::TYPE_INTEGER;
	public $fontAwesome = FontAwesome::AGGREGATE_CORRELATION;
	public $htmlType = 'text';
	public $image = ImageUrls::AGGREGATE_CORRELATION;
	public $inForm = true;
	public $inIndex = true;
	public $inView = true;
	public $isFillable = true;
	public $isOrderable = true;
	public $isSearchable = false;
	public $maximum = 2147483647;
	public $minimum = -2147483648;
	public $name = self::NAME;
	public const NAME = 'onset_delay_with_strongest_pearson_correlation';
	public $phpType = \App\Types\PhpTypes::INTEGER;
	public $rules = 'nullable|integer|min:-2147483648|max:2147483647';
	public $title = 'Onset Delay With Strongest Pearson UserVariableRelationship';
	public $type = self::TYPE_INTEGER;
	public $canBeChangedToNull = true;
	public $validations = 'nullable|integer|min:-2147483648|max:2147483647';

}
