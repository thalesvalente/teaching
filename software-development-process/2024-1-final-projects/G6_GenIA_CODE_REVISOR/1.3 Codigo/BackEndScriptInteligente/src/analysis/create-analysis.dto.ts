import { IsString, IsNumber } from 'class-validator';

export class CreateAnalysisDto {
  @IsString()
  result: string;

  @IsNumber()
  scriptId: number;
}
