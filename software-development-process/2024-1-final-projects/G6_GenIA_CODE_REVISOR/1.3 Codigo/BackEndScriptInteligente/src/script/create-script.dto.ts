import { IsString } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';

export class CreateScriptDto {
  @IsString()
  @ApiProperty({
    description: 'Content of the script',
    example: 'console.log("Hello, world!");',
  })
  content: string;
}
